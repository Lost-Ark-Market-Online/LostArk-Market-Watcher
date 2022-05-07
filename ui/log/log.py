# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtGui import QColor
from datetime import datetime
from ui.common.draggablewindow import DraggableWindow
from ui.common.uiloader import UiLoader
import ui.log.resources


class LostArkMarketWatcherLog(QMainWindow):
    def __init__(self, version, region):
        super(LostArkMarketWatcherLog, self).__init__()
        self.version = version
        self.region = region
        self.load_ui()
        self.setWindowTitle("Log - LostArkMarketOnline")

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
            f"Lost Ark Market Watcher v{self.version} - {self.region} - Log")
        ui_file.close()
        return widget

    def close(self):
        self.hide()

    def log(self, txt, error=False, save_log=False):
        log_txt = f'{datetime.now().strftime("%m/%d/%Y-%H:%M:%S")} - {txt}'
        print(log_txt)
        i = QListWidgetItem(log_txt)
        if error:
            i.setForeground(QColor('#FFFFFF'))
            i.setBackground(QColor('#ED4337'))
            if save_log:
                with open(f'{datetime.now().strftime("%m-%d-%Y")}.error', "a") as file_object:
                    file_object.write(f"{log_txt}\n")
        else:
            i.setForeground(QColor('#00FF00'))
            if save_log:
                with open(f'{datetime.now().strftime("%m-%d-%Y")}.log', "a") as file_object:
                    file_object.write(f"{log_txt}\n")
        self.lLog.addItem(i)
        self.lLog.scrollToBottom()


if __name__ == "__main__":
    app = QApplication([])
    widget = LostArkMarketWatcherLog()
    sys.exit(app.exec_())
