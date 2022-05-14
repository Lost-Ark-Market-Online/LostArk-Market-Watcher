import os
from pathlib import Path

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtGui import QIcon
from modules.sound import VolumeController

from ui.common.draggablewindow import DraggableWindow
from ui.common.uiloader import UiLoader
import ui.config.resources
from modules.config import Config


class LostArkMarketWatcherConfig(QMainWindow):
    config_updated = Signal()

    def __init__(self):
        super(LostArkMarketWatcherConfig, self).__init__()
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
        widget.btnCustomScreenshotFolder.clicked.connect(
            self.open_screenshots_directory_dialog)
        widget.btnGameFolder.clicked.connect(self.open_game_directory_dialog)

        widget.cbPlaySounds.stateChanged.connect(
            self.audio_toggle)
            
        widget.cbCustomScreenshotFolder.stateChanged.connect(
            self.screenshot_folder_toggle)

        self.slVolume.valueChanged.connect(self.update_volume)
        widget.lblTitle.setText(
            f'Lost Ark Market Watcher v{Config().version} - {Config().region}')
        return widget

    def audio_toggle(self, value):
        if value == 0:
            self.lblVolume.setVisible(0)
            self.slVolume.setVisible(0)
        else:
            self.lblVolume.setVisible(1)
            self.slVolume.setVisible(1)

    def update_volume(self, value):
        VolumeController().setVolume(value / 100)

    def screenshot_folder_toggle(self, value):
        if value == 0:
            self.txtCustomScreenshotFolder.setVisible(0)
            self.btnCustomScreenshotFolder.setVisible(0)
        else:
            self.txtCustomScreenshotFolder.setText(None)
            self.txtCustomScreenshotFolder.setVisible(1)
            self.btnCustomScreenshotFolder.setVisible(1)

    def open_screenshots_directory_dialog(self):
        fileName = QFileDialog.getExistingDirectory(
            self, "Select the Lost Ark Screenshot Directory")
        self.txtCustomScreenshotFolder.setText(fileName)

    def open_game_directory_dialog(self):
        fileName = QFileDialog.getExistingDirectory(
            self, "Select the Lost Ark Game Directory")
        self.txtGameFolder.setText(fileName)

    def save_config(self):
        Config().update_config({
            "play_audio": self.cbPlaySounds.isChecked(),
            "delete_screenshots": self.cbDeleteScreenshots.isChecked(),
            "screenshots_directory": self.txtCustomScreenshotFolder.text() if self.cbCustomScreenshotFolder.isChecked() else None,
            "game_directory": self.txtGameFolder.text(),
            "screenshot_threads": self.sbScreenshotThreads.value(),
            "scan_threads": self.sbScanningThreads.value(),
            "upload_threads": self.sbUploadingThreads.value(),
            "volume": self.slVolume.value(),
        })
        self.config_updated.emit()
        self.close()

    def cancel(self):
        self.close()

    def show_ui(self):
        self.txtGameFolder.setText(Config().game_directory)
        if(Config().screenshots_directory):
            self.txtCustomScreenshotFolder.setText(
                Config().screenshots_directory)
            self.cbCustomScreenshotFolder.setChecked(True)
            self.txtCustomScreenshotFolder.setVisible(1)
            self.btnCustomScreenshotFolder.setVisible(1)
        else:
            self.cbCustomScreenshotFolder.setChecked(False)
            self.txtCustomScreenshotFolder.setVisible(0)
            self.btnCustomScreenshotFolder.setVisible(0)

        self.cbDeleteScreenshots.setChecked(Config().delete_screenshots)
        self.cbLog.setChecked(Config().save_log)
        self.sbScreenshotThreads.setValue(Config().screenshot_threads)
        self.sbScanningThreads.setValue(Config().scan_threads)
        self.sbUploadingThreads.setValue(Config().upload_threads)

        self.cbPlaySounds.setChecked(Config().play_audio)
        self.slVolume.setValue(Config().volume)
        self.show()
