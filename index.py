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
from modules.sound import playCheck, playError, playPulse, playSuccess

from ui.config.config import LostArkMarketWatcherConfig

version = '0.4.1'


class LostArkMarketWatcher(QApplication):
    market_db = None
    observer = None
    config_form = None
    play_audio = True
    delete_screenshots = True
    screenshots_directory = None
    screenshot_executor = None

    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        self.setQuitOnLastWindowClosed(False)
        self.build_menu()
        self.market_db = MarketDb()
        self.safe_spawn_observer()

    def build_menu(self):
        icon = QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                  "assets/icons/favicon.png")))
        self.tray = QSystemTrayIcon()
        menu = QMenu()
        config_action = menu.addAction("Configuration")
        config_action.triggered.connect(self.open_config)
        separator = menu.addSeparator()
        close_action = menu.addAction("Close")
        close_action.triggered.connect(self.close_action)
        self.tray.setIcon(icon)
        self.tray.setContextMenu(menu)
        self.tray.show()
        self.tray.setToolTip("Lost Ark Market Watcher")

    def open_config(self):
        self.config_form = LostArkMarketWatcherConfig(
            version, self.market_db.region, self.play_audio, self.delete_screenshots, self.screenshots_directory
        )
        self.config_form.config_updated.connect(self.safe_spawn_observer)
        self.config_form.ui.show()

    def close_action(self):
        os._exit(1)

    def safe_spawn_observer(self):
        try:
            self.spawn_observer()
        except NotConfigured:
            self.open_config()

    def spawn_observer(self):
        self.play_audio, self.delete_screenshots, self.screenshots_directory = get_config()

        if self.screenshots_directory == None:
            if self.play_audio == True:
                playError()
            raise NotConfigured()

        event_handler = FileSystemEventHandler()
        event_handler.on_created = self.on_created

        if self.observer is not None and self.observer.is_alive() == True:
            self.observer.stop()

        self.observer = Observer()
        self.observer.schedule(
            event_handler, self.screenshots_directory, recursive=False)

        self.observer.start()
        self.screenshot_executor = ThreadPoolExecutor(max_workers=1)

        if self.play_audio == True:
            playSuccess()

    def on_created(self, event):
        self.screenshot_executor.submit(
            self.process_screenshot, event.src_path)

    def process_screenshot(self, file):
        try:
            print('== New screenshoot found ==')
            time.sleep(2)
            if self.play_audio == True:
                playCheck()

            print('== Scanning: Start ==')
            res = scan(file)
            print('== Scanning: Finish ==')
            entry_futures = []
            entries_executor = ThreadPoolExecutor(max_workers=2)
            for item in res:
                entry_futures.append(entries_executor.submit(
                    self.market_db.add_entry, item, self.play_audio))
            wait(entry_futures)
            print("== Finished ==")
            if self.play_audio == True:
                playSuccess()
            time.sleep(1)
            os.remove(file)
        except:
            playError()
            traceback.print_exc()


if __name__ == "__main__":
    app = LostArkMarketWatcher([])
    sys.exit(app.exec())
