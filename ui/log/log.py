# This Python file uses the following encoding: utf-8
import logging
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtGui import QColor
from datetime import datetime
from modules.config import Config
from modules.logging import AppLogger
from ui.common.draggablewindow import DraggableWindow
from ui.common.uiloader import UiLoader
import ui.log.resources


class LostArkMarketWatcherLog(QMainWindow):
    signal = Signal(str, int)

    def __init__(self):
        super(LostArkMarketWatcherLog, self).__init__()
        self.load_ui()
        self.setWindowTitle("Log - LostArkMarketOnline")
        self.signal.connect(self.log)

    def load_ui(self):
        loader = UiLoader(self)
        loader.registerCustomWidget(DraggableWindow)
        path = os.fspath(Path(__file__).resolve().parent /
                         "../../assets/ui/log.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        widget = loader.load(ui_file)
        widget.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        widget.btnClose.clicked.connect(self.close)
        widget.lLog.setWordWrap(True)
        widget.lLog.setAutoScroll(True)
        widget.lLog.setAutoScrollMargin(20)
        widget.lblTitle.setText(
            f"Lost Ark Market Watcher v{Config().version} - {Config().region} - Log")
        ui_file.close()
        return widget

    def close(self):
        self.hide()

    def log(self, txt, level):
        i = QListWidgetItem(txt)
        if level <= logging.INFO:
            i.setForeground(QColor('#00FF00'))
        else:
            i.setForeground(QColor('#FFFFFF'))
            i.setBackground(QColor('#ED4337'))
        self.lLog.addItem(i)
        self.lLog.scrollToBottom()


if __name__ == "__main__":
    app = QApplication([])
    widget = LostArkMarketWatcherLog()
    sys.exit(app.exec_())
