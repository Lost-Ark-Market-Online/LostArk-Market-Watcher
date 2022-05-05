from datetime import datetime
import sys
import time
import os
import traceback

from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PySide6.QtGui import QIcon

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from concurrent.futures import ThreadPoolExecutor, wait

from modules.config import get_config
from modules.db import MarketDb
from modules.errors import NotConfigured
from modules.scan import scan
from modules.sound import playCheck, playError, playSuccess

from ui.config.config import LostArkMarketWatcherConfig
from ui.log.log import LostArkMarketWatcherLog

version = '0.5.0'
debug = False


class LostArkMarketWatcher(QApplication):
    market_db = None
    observer = None
    config_form = None
    play_audio = True
    save_log = False
    delete_screenshots = True
    screenshots_directory = None
    screenshot_executor = None

    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        self.setQuitOnLastWindowClosed(False)
        self.build_menu()
        self.market_db = MarketDb(version)
        self.log_view = LostArkMarketWatcherLog(version, self.market_db.region)
        self.config_form = LostArkMarketWatcherConfig(
            version, self.market_db.region)
        self.config_form.config_updated.connect(self.spawn_observer)
        self.market_db.log.connect(self.write_log)
        self.market_db.error.connect(self.write_error)
        self.spawn_observer()

    def get_config(self):
        self.play_audio, self.delete_screenshots, self.screenshots_directory, self.save_log = get_config()

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
        self.log_view.ui.show()

    def open_config(self):
        self.get_config()
        self.config_form.show(self.play_audio, self.delete_screenshots,
                              self.screenshots_directory, self.save_log)

    def close_action(self):
        os._exit(1)

    def spawn_observer(self):
        self.get_config()

        if self.screenshots_directory == None:
            if self.play_audio == True:
                playError()
            self.write_log('Screenshots directory not found')
            self.open_config()
            return

        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_created

        if self.observer is not None and self.observer.is_alive() == True:
            self.write_log('Watcher unloaded')
            self.observer.stop()

        self.observer = Observer()
        self.observer.schedule(
            event_handler, self.screenshots_directory, recursive=False)

        self.write_log('Watcher Started')
        self.observer.start()
        self.screenshot_executor = ThreadPoolExecutor(max_workers=1)

        if self.play_audio == True:
            playSuccess()

    def on_created(self, event):
        self.screenshot_executor.submit(
            self.process_screenshot, event.src_path)

    def process_screenshot(self, file):
        try:
            self.write_log('New screenshoot found')
            time.sleep(2)
            if self.play_audio == True:
                playCheck()

            self.write_log('Scanning: Start')
            res = scan(file, debug, self.write_log, self.write_error)
            self.write_log('Scanning: Finish')
            entry_futures = []
            entries_executor = ThreadPoolExecutor(max_workers=2)
            for item in res:
                entry_futures.append(entries_executor.submit(
                    self.market_db.add_entry, item, self.play_audio))
            wait(entry_futures)
            self.write_log("Finished")
            if self.play_audio == True:
                playSuccess()
            time.sleep(1)
            os.remove(file)
        except:
            playError()
            self.write_error(traceback.format_exc())

    def write_log(self, txt):
        self.log_view.log(txt, False, self.save_log)

    def write_error(self, txt):
        self.log_view.log(txt, True, self.save_log)


if __name__ == "__main__":
    app = LostArkMarketWatcher([])
    sys.exit(app.exec())
