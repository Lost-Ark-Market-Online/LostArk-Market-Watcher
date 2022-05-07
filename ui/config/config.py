import os
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtGui import QIcon

from ui.common.draggablewindow import DraggableWindow
from ui.common.uiloader import UiLoader
import ui.config.resources
from modules.config import update_config


class LostArkMarketWatcherConfig(QMainWindow):
    config_updated = Signal()

    def __init__(self, version, region):
        super(LostArkMarketWatcherConfig, self).__init__()
        self.region = region
        self.version = version
        self.load_ui()
        self.setWindowTitle("Config - LostArkMarketOnline")
        

    def load_ui(self):
        loader = UiLoader(self)
        path = os.fspath(Path(__file__).resolve().parent /
                         "../../assets/ui/config.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.registerCustomWidget(DraggableWindow)
        widget = loader.load(ui_file)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        ui_file.close()
        widget.btnSave.clicked.connect(self.save_config)
        widget.btnCancel.clicked.connect(self.cancel)
        widget.btnClose.clicked.connect(self.cancel)
        widget.btnFile.clicked.connect(self.open_file_dialog)
        widget.lblTitle.setText(
            f'Lost Ark Market Watcher v{self.version} - {self.region}')
        return widget

    def open_file_dialog(self):
        fileName = QFileDialog.getExistingDirectory(
            self, "Select the Lost Ark Screenshot Directory")
        self.txtFile.setText(fileName)

    def save_config(self):
        update_config({
            "play_audio": str(self.cbPlaySounds.isChecked()),
            "delete_screenshots": str(self.cbDeleteScreenshots.isChecked()),
            "screenshots_directory": self.txtFile.text(),
            "save_log": str(self.cbLog.isChecked()),
        })
        self.config_updated.emit()
        self.close()

    def cancel(self):
        self.close()

    def show_ui(self, play_audio, delete_screenshots, screenshots_directory, save_log):
        self.txtFile.setText(screenshots_directory)
        self.cbPlaySounds.setChecked(play_audio)
        self.cbDeleteScreenshots.setChecked(delete_screenshots)
        self.cbLog.setChecked(save_log)
        self.show()
