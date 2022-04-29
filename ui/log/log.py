# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtCore import QFile, Qt, Signal
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QColor
from datetime import datetime
from ui.common.draggablewindow import DraggableWindow
import ui.log.resources


class LostArkMarketWatcherLog(QMainWindow):
    def __init__(self, version, region):
        super(LostArkMarketWatcherLog, self).__init__()
        self.version = version
        self.region = region
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        loader.registerCustomWidget(DraggableWindow)
        path = os.fspath(Path(__file__).resolve().parent /
                         "../../assets/ui/log.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        self.ui.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.lLog.setWordWrap(True)
        self.ui.lblTitle.setText(
            f"Lost Ark Market Watcher v{self.version} - {self.region} - Log")
        ui_file.close()

    def close(self):
        self.ui.hide()

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
        self.ui.lLog.addItem(i)


if __name__ == "__main__":
    app = QApplication([])
    widget = LostArkMarketWatcherLog()
    sys.exit(app.exec_())
