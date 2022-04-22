import time
import os
import easygui
import traceback
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from modules.config import change_region, change_screenshot_dir, checkconfig
from modules.db import MarketDb
from modules.scan import scan
from modules.sound import playCheck, playError, playPulse, playSuccess

import pystray
from PIL import Image

version = '0.2.0'
screenshootsdir, region = checkconfig()
firestore = None
observer = None

RUNNING = True


def on_created(event):
    try:
        print('== New screenshoot found ==')
        time.sleep(2)
        playCheck()
        print('== Scanning ==')
        res = scan(event.src_path)
        for item in res:
            playPulse()
            print(item)
            firestore.add_entry(item)
        playSuccess()
        time.sleep(1)
        os.remove(event.src_path)
    except:
        playError()
        traceback.print_exc()


def spawn_observer():
    global observer

    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created

    observer = Observer()
    observer.schedule(event_handler, screenshootsdir, recursive=False)
    observer.start()

def app_setup():
    global firestore

    def close_action():
        os._exit(1)

    def about_action():
        easygui.msgbox(title=f'Lost Ark Market Watcher - {version}',
                       msg='App made for scanning the game screenshoots and look for market data to feed the Lost Ark Market Webapp.')

    def change_region_action():
        global region
        global firestore
        region = change_region(region)
        firestore = MarketDb(region)

    def change_screenshot_dir_action():
        global screenshootsdir
        screenshootsdir = change_screenshot_dir(screenshootsdir)
        if(observer is not None):
            observer.stop()
        spawn_observer()

    image = Image.open(os.path.abspath(os.path.join(os.path.dirname(__file__),'assets/icons/favicon.png')))
    firestore = MarketDb(region)

    menu = (
        pystray.MenuItem('About', about_action),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('Change User', firestore.login),
        pystray.MenuItem('Change Region', change_region_action),
        pystray.MenuItem('Change Screenshot File', change_screenshot_dir_action),
        pystray.Menu.SEPARATOR,
        pystray.MenuItem('Close', close_action),
    )

    icon = pystray.Icon("MarketWatcher", image,
                        "Lost Ark Market Watcher", menu)

    spawn_observer()
    icon.run()


if __name__ == "__main__":  
    app_setup()
