import configparser
import os
from modules.common.singleton import Singleton
from modules.errors import NoTokenError
from modules.find_game import find_lostark_directory
import xml.etree.ElementTree as ET

game_region_map = {
    "SA": "South America",
    "EA": "North America East",
    "WA": "North America West",
    "CE": "Europe Central",
    "WE": "Europe West"
}


class Config(metaclass=Singleton):
    version = "0.8.20.2"
    region: str
    game_region: str
    debug = False
    id_token: str
    refresh_token: str
    uid: str
    play_audio: bool
    save_log: bool
    delete_screenshots: bool
    volume: float
    screenshot_threads: int
    scan_threads: int
    upload_threads: int
    screenshots_directory: str
    game_directory: str
    open_log_on_start: bool
    _config: configparser.ConfigParser

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read("config.ini")
        self.load_config()

    def load_config(self):
        changes = False

        if self._config.has_section("Token"):
            self.id_token = self._config.get("Token", "id_token")
            self.refresh_token = self._config.get("Token", "refresh_token")
            self.uid = self._config.get("Token", "uid")
        else:
            raise NoTokenError()

        if self._config.has_section("Watcher"):
            if self._config.has_option("Watcher", "play_audio"):
                self.play_audio = self._config.get(
                    "Watcher", "play_audio") == 'True'
            else:
                self.play_audio = True
                changes = True

            if self._config.has_option("Watcher", "volume"):
                self.volume = float(self._config.get(
                    "Watcher", "volume"))
            else:
                self.volume = 100
                changes = True

            if self._config.has_option("Watcher", "delete_screenshots"):
                self.delete_screenshots = self._config.get(
                    "Watcher", "delete_screenshots") == 'True'
            else:
                self.delete_screenshots = False
                changes = True

            if self._config.has_option("Watcher", "save_log"):
                self.save_log = self._config.get(
                    "Watcher", "save_log") == 'True'
            else:
                self.save_log = False
                changes = True

            if self._config.has_option("Watcher", "scan_threads"):
                self.scan_threads = int(self._config.get(
                    "Watcher", "scan_threads"))
            else:
                self.scan_threads = 2
                changes = True

            if self._config.has_option("Watcher", "screenshot_threads"):
                self.screenshot_threads = int(self._config.get(
                    "Watcher", "screenshot_threads"))
            else:
                self.screenshot_threads = 1
                changes = True

            if self._config.has_option("Watcher", "upload_threads"):
                self.upload_threads = int(self._config.get(
                    "Watcher", "upload_threads"))
            else:
                self.upload_threads = 2
                changes = True

            if self._config.has_option("Watcher", "screenshots_directory"):
                self.screenshots_directory = self._config.get(
                    "Watcher", "screenshots_directory")
            else:
                self.screenshots_directory = None

            if self._config.has_option("Watcher", "game_directory"):
                self.game_directory = self._config.get(
                    "Watcher", "game_directory")
            else:
                self.game_directory = find_lostark_directory()
                changes = True

            if self._config.has_option("Watcher", "open_log_on_start"):
                self.open_log_on_start = self._config.get(
                    "Watcher", "open_log_on_start") == 'True'
            else:
                self.open_log_on_start = False
                changes = True
                
            if self._config.has_option("Watcher", "debug"):
                self.debug = self._config.get(
                    "Watcher", "debug") == 'True'
            else:
                self.debug = False
                changes = True

            

            self.get_game_region()
        else:
            self.play_audio = True
            self.volume = 100
            self.delete_screenshots = False
            self.save_log = False
            self.scan_threads = 2
            self.screenshot_threads = 1
            self.upload_threads = 2
            self.screenshots_directory = None
            self.open_log_on_start = False
            self.game_directory = find_lostark_directory()
            changes = True        

        if changes:
            self.update_config_file()

    def update_config_file(self):
        if self._config.has_section("Token") == False:
            self._config.add_section("Token")
        self._config.set("Token", "refresh_token", self.refresh_token)
        self._config.set("Token", "id_token", self.id_token)
        self._config.set("Token", "uid", self.uid)

        if self._config.has_section("Watcher") == False:
            self._config.add_section("Watcher")
        
        self.set_or_remove_config_option(
            "Watcher", "play_audio", self.play_audio
        )
        self.set_or_remove_config_option(
            "Watcher", "volume", self.volume
        )
        self.set_or_remove_config_option(
            "Watcher", "delete_screenshots", self.delete_screenshots
        )
        self.set_or_remove_config_option(
            "Watcher", "save_log", self.save_log
        )
        self.set_or_remove_config_option(
            "Watcher", "scan_threads", self.scan_threads
        )
        self.set_or_remove_config_option(
            "Watcher", "screenshot_threads", self.screenshot_threads
        )
        self.set_or_remove_config_option(
            "Watcher", "upload_threads", self.upload_threads
        )
        self.set_or_remove_config_option(
            "Watcher", "game_directory", self.game_directory
        )
        self.set_or_remove_config_option(
            "Watcher", "screenshots_directory", self.screenshots_directory
        )
        self.set_or_remove_config_option(
            "Watcher", "open_log_on_start", self.open_log_on_start
        )
        with open("config.ini", "w") as configfile:
            self._config.write(configfile)

    def set_or_remove_config_option(self, section, option, value):
        if value is None:
            self._config.remove_option(section, option)
        else:
            self._config.set(section, option, str(value))

    def update_token(self, token):
        self.id_token = token["id_token"]
        self.refresh_token = token["refresh_token"]
        self.uid = token["uid"]
        self.update_config_file()

    def update_config(self, new_config):
        if "play_audio" in new_config:
            self.play_audio = new_config["play_audio"]
        if "volume" in new_config:
            self.volume = new_config["volume"]
        if "delete_screenshots" in new_config:
            self.delete_screenshots = new_config["delete_screenshots"]
        if "save_log" in new_config:
            self.save_log = new_config["save_log"]
        if "scan_threads" in new_config:
            self.scan_threads = new_config["scan_threads"]
        if "screenshot_threads" in new_config:
            self.screenshot_threads = new_config["screenshot_threads"]
        if "upload_threads" in new_config:
            self.upload_threads = new_config["upload_threads"]
        if "screenshots_directory" in new_config:
            self.screenshots_directory = new_config["screenshots_directory"]
        if "game_directory" in new_config:
            self.game_directory = new_config["game_directory"]
        if "open_log_on_start" in new_config:
            self.open_log_on_start = new_config["open_log_on_start"]
        self.update_config_file()

    def get_game_region(self):
        try:
            tree = ET.parse(os.path.abspath(os.path.join(
                self.game_directory, 'EFGame', 'Config', 'UserOption.xml')))
            root = tree.getroot()
            game_region_id = root.find(
                'SaveAccountOptionData').findtext('RegionID')
            self.game_region = game_region_map.get(game_region_id)
        except:
            self.game_directory = None
            self.game_region = None


Config()
