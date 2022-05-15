
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow
from PySide6.QtCore import Qt

from modules.config import Config


class MessageBoxHandler(QObject):
    app: QApplication
    msgBox: QMessageBox

    def __init__(self, message_box):
        self.app = QApplication.instance()
        self.msgBox = QMessageBox()
        self.msgBox.hide()
        message_box.connect(self.spawn_message_box)
        pass

    def spawn_message_box(self, data):
        match data["type"]:
            case "REGION":
                self.wrong_region()
                return
            case "GAME_DIRECTORY":
                self.game_directory_not_found()
                return
            case "VERSION":
                self.new_version(data)
                return

    def wrong_region(self):        
        self.msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.msgBox.setWindowTitle("Lost Ark Market Online")
        self.msgBox.setText(f"Region missmatch")
        self.msgBox.setInformativeText(
            f"Your account is authorized to post in the {Config().region} region, but your current region is {Config().game_region}")
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.exec()

    def game_directory_not_found(self):        
        self.msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.msgBox.setWindowTitle("Lost Ark Market Online")
        self.msgBox.setText(f"Game Directory not found")
        self.msgBox.setInformativeText(
            f"The app couldn't find the game directory, please select it manually. Ex: C:\\Program Files (x86)\\Steam\\steamapps\\common\\Lost Ark")
        self.msgBox.setIcon(QMessageBox.Warning)
        self.msgBox.exec()

    def new_version(self, data):
        self.msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.msgBox.setWindowTitle("Lost Ark Market Online")
        self.msgBox.setText(f"New version v{data['new_version']} available.")
        self.msgBox.setInformativeText(
            "Please close the app and run the launcher to download the new version.")
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.exec()
