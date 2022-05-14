
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
        # self.msgBox.show()
        # self.msgBox.activateWindow()
        # self.msgBox.raise_()
        # self.app.setActiveWindow(self.msgBox)
        self.msgBox.exec()

    def new_version(self, data):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Lost Ark Market Online")
        msgBox.setText(f"New version v{data['new_version']} available.")
        msgBox.setInformativeText(
            "Please close the app and run the launcher to download the new version.")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.exec()
