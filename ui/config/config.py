import os
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtUiTools import QUiLoader

from ui.common.draggablewindow import DraggableWindow
import ui.config.resources
from modules.config import update_config


class LostArkMarketWatcherConfig(QMainWindow):
    config_updated = Signal()

    def __init__(self, version, region):
        super(LostArkMarketWatcherConfig, self).__init__()
        self.load_ui()
        self.ui.btnSave.clicked.connect(self.save_config)
        self.ui.btnCancel.clicked.connect(self.cancel)
        self.ui.btnClose.clicked.connect(self.cancel)
        self.ui.btnFile.clicked.connect(self.open_file_dialog)
        self.ui.lblTitle.setText(
            f'Lost Ark Market Watcher v{version} - {region}')

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent /
                         "../../assets/ui/config.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.registerCustomWidget(DraggableWindow)
        self.ui = loader.load(ui_file, self)
        self.ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        ui_file.close()

    def open_file_dialog(self):
        fileName = QFileDialog.getExistingDirectory(
            self, "Select the Lost Ark Screenshot Directory")
        self.ui.txtFile.setText(fileName)

    def save_config(self):
        update_config({
            "play_audio": str(self.ui.cbPlaySounds.isChecked()),
            "delete_screenshots": str(self.ui.cbDeleteScreenshots.isChecked()),
            "screenshots_directory": self.ui.txtFile.text(),
            "save_log": str(self.ui.cbLog.isChecked()),
        })
        self.config_updated.emit()
        self.ui.close()

    def cancel(self):
        self.ui.close()

    def show(self, play_audio, delete_screenshots, screenshots_directory, save_log):
        self.ui.txtFile.setText(screenshots_directory)
        self.ui.cbPlaySounds.setChecked(play_audio)
        self.ui.cbDeleteScreenshots.setChecked(delete_screenshots)
        self.ui.cbLog.setChecked(save_log)
        self.ui.show()
