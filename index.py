import modules.single_instance

from datetime import datetime
import sys
import time
import os
import traceback
import ctypes

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from concurrent.futures import ThreadPoolExecutor, wait

from modules.config import Config
from modules.db import MarketDb
from modules.messagebox import MessageBoxHandler
from modules.scan import scan
from modules.sound import VolumeController, playCheck, playError, playSuccess

from ui.config.config import LostArkMarketWatcherConfig
from ui.log.log import LostArkMarketWatcherLog


class LostArkMarketWatcher(QApplication):
    market_db = None
    observer = None
    config_form = None
    screenshot_executor = None
    message_box = Signal(dict)
    message_box_handler: MessageBoxHandler
    volume_controller: VolumeController

    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        self.setQuitOnLastWindowClosed(False)
        self.build_menu()
        self.market_db = MarketDb()
        self.message_box_handler = MessageBoxHandler(self.message_box)
        self.log_view = LostArkMarketWatcherLog()
        self.config_form = LostArkMarketWatcherConfig()
        self.volume_controller = VolumeController()
        self.config_form.config_updated.connect(self.spawn_observer)
        self.market_db.log.connect(self.write_log)
        self.market_db.error.connect(self.write_error)
        self.market_db.new_version.connect(self.new_version)
        self.spawn_observer()

    def build_menu(self):
        icon = QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  "assets/icons/favicon.png")))
        self.tray = QSystemTrayIcon()
        menu = QMenu()
        config_action = menu.addAction("Configuration")
        config_action.triggered.connect(self.open_config)
        log_action = menu.addAction("Log")
        log_action.triggered.connect(self.open_log)
        menu.addSeparator()
        close_action = menu.addAction("Close")
        close_action.triggered.connect(self.close_action)
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.setToolTip("Lost Ark Market Watcher")

    def open_log(self):
        self.log_view.show()

    def open_config(self):
        self.config_form.show_ui()

    def close_action(self):
        self.tray.hide()
        os._exit(1)

    def spawn_observer(self):
        screenshots_directory = None
        if Config().screenshots_directory:
            screenshots_directory = Config().screenshots_directory
        else:
            if Config().game_directory:
                screenshots_directory = os.path.abspath(os.path.join(
                    Config().game_directory, 'EFGame', 'Screenshots'))
            else:
                self.write_log('Screenshots directory not found')
                if Config().play_audio == True:
                    playError()
                self.open_config()
                return
        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_created

        if self.observer is not None and self.observer.is_alive() == True:
            self.write_log('Watcher unloaded')
            self.observer.stop()

        self.observer = Observer()
        self.observer.schedule(
            event_handler, screenshots_directory, recursive=False)

        self.write_log('Watcher Started')
        self.observer.start()
        self.screenshot_executor = ThreadPoolExecutor(
            max_workers=Config().screenshot_threads)

        if Config().play_audio == True:
            playSuccess()

    def on_created(self, event):
        # Region Check
        Config().get_game_region()
        if Config().game_region == Config().region:
            self.screenshot_executor.submit(
                self.process_screenshot, event.src_path)
        else:
            if Config().game_directory is None:
                if Config().play_audio == True:
                    playError()
                self.open_config()
                self.message_box.emit({"type": "GAME_DIRECTORY"})
            else:
                self.message_box.emit({"type": "REGION"})

    def process_screenshot(self, file):
        try:
            self.write_log('New screenshoot found')
            time.sleep(2)
            if Config().play_audio == True:
                playCheck()

            self.write_log('Scanning: Start')
            res = scan(file, self.write_log, self.write_error)
            self.write_log('Scanning: Finish')
            entry_futures = []
            entries_executor = ThreadPoolExecutor(
                max_workers=Config().upload_threads)
            for item in res:
                entry_futures.append(entries_executor.submit(
                    self.market_db.add_entry, item))
            wait(entry_futures)
            self.write_log("Finished")
            if Config().play_audio == True:
                playSuccess()
            time.sleep(1)
            if Config().delete_screenshots == True:
                os.remove(file)
        except:
            if Config().play_audio == True:
                playError()
            self.write_error(traceback.format_exc())

    def write_log(self, txt):
        self.log_view.log(txt, False)

    def write_error(self, txt):
        self.log_view.log(txt, True)

    def new_version(self, new_version):
        self.message_box.emit({"type": "REGION", "new_version": new_version})


if __name__ == "__main__":
    myappid = f'lostarkmarketonline.watcher.app.{Config().version}'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    app = LostArkMarketWatcher([])
    icon = QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                              "assets/icons/favicon.png")))
    app.setWindowIcon(icon)
    sys.exit(app.exec())
