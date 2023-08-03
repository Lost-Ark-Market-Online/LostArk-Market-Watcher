from shutil import rmtree
import modules.single_instance
import faulthandler
from datetime import datetime
import sys
import time
import os
import traceback
import ctypes
from raven import Client

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal
from thefuzz import fuzz

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from concurrent.futures import ThreadPoolExecutor, wait

from modules.config import Config
from modules.logging import AppLogger
from modules.db import MarketDb
from modules.messagebox import MessageBoxHandler
from modules.scan import scan_file
from modules.sound import VolumeController, playCheck, playError, playSuccess

from ui.config.config import LostArkMarketWatcherConfig
from ui.log.log import LostArkMarketWatcherLog


class LostArkMarketWatcher(QApplication):
    market_db = None
    observer = None
    config_form = None
    screenshot_executor = None
    message_box = Signal(dict)
    open_config = Signal()
    message_box_handler: MessageBoxHandler

    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        self.setQuitOnLastWindowClosed(False)
        self.build_menu()
        self.market_db = MarketDb()
        self.message_box_handler = MessageBoxHandler(self.message_box)

        self.log_view = LostArkMarketWatcherLog()
        AppLogger().signal_enable(self.log_view.signal)
        self.config_form = LostArkMarketWatcherConfig(self.open_config)
        self.config_form.config_updated.connect(self.spawn_observer)
        self.market_db.new_version.connect(self.new_version)
        if Config().open_log_on_start:
            self.open_log()
        self.spawn_observer()

    def build_menu(self):
        icon = QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  "assets/icons/favicon.png")))
        self.tray = QSystemTrayIcon()
        menu = QMenu()
        config_action = menu.addAction("Configuration")
        config_action.triggered.connect(self.open_config_form)
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

    def open_config_form(self):
        self.open_config.emit()

    def close_action(self):
        self.tray.hide()
        os._exit(1)

    def spawn_observer(self):

        AppLogger().refresh_handlers()
        screenshots_directory = None
        if Config().screenshots_directory:
            screenshots_directory = Config().screenshots_directory
        else:
            if Config().game_directory:
                screenshots_directory = os.path.abspath(os.path.join(
                    Config().game_directory, 'EFGame', 'Screenshots'))
            else:
                AppLogger().error('Screenshots directory not found')
                if Config().play_audio == True:
                    playError()
                self.open_config.emit()
                return
        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_created

        if self.observer is not None and self.observer.is_alive() == True:
            AppLogger().info('Watcher unloaded')
            self.observer.stop()

        self.observer = Observer()
        self.observer.schedule(
            event_handler, screenshots_directory, recursive=False)

        AppLogger().info('Watcher Started')
        self.observer.start()
        self.screenshot_executor = ThreadPoolExecutor(
            max_workers=Config().screenshot_threads)

        if Config().play_audio == True:
            playSuccess()

    def on_created(self, event):
        # Region Check
        AppLogger().info('New screenshoot found')
        Config().get_game_region()
        AppLogger().info(f'Game Region Detected: {Config().game_region}')
        if Config().game_directory and (fuzz.ratio(Config().game_region, Config().region) > 98):
            AppLogger().info('Region check successful')
            self.screenshot_executor.submit(
                self.process_screenshot, event.src_path)
        else:
            if Config().game_directory is None:
                AppLogger().error('No Game Directory')
                if Config().play_audio == True:
                    playError()
                self.open_config.emit()
                self.message_box.emit({"type": "GAME_DIRECTORY"})
            else:
                AppLogger().error('Game Directory found, wrong region')
                self.message_box.emit({"type": "REGION"})

    def process_screenshot(self, file):
        try:
            time.sleep(2)
            if Config().play_audio == True:
                playCheck()
            AppLogger().info('Scanning: Start')
            res = scan_file(file)
            AppLogger().info('Scanning: Finish')
            entry_futures = []
            entries_executor = ThreadPoolExecutor(
                max_workers=Config().upload_threads)
            for item in res:
                entry_futures.append(entries_executor.submit(
                    self.market_db.add_entry, item))
            wait(entry_futures)
            AppLogger().info("Finished")
            if Config().play_audio == True:
                playSuccess()
            time.sleep(1)
            if Config().delete_screenshots == True:
                os.remove(file)
        except Exception as ex:
            if Config().play_audio == True:
                playError()
            AppLogger().exception(ex)
            AppLogger().client.capture_exceptions()

    def new_version(self, new_version):
        self.message_box.emit({"type": "REGION", "new_version": new_version})


if __name__ == "__main__":
    AppLogger()
    try:
        myappid = f'lamo.watcher.app.{Config().version}'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        app = LostArkMarketWatcher([])
        icon = QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  "assets/icons/favicon.png")))
        app.setWindowIcon(icon)
        
        if Config().debug:
            AppLogger().debug('Directories cleanup')
            if os.path.isdir('debug'):
                rmtree('debug')
            os.mkdir('debug')
            os.mkdir('debug/inspection')
        sys.exit(app.exec())
    except Exception as e:
        AppLogger().exception(e)
        AppLogger().client.capture_exceptions()
