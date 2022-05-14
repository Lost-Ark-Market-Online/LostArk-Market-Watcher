
import os
from tendo.singleton import SingleInstance
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from modules.sound import playError


try:
    me = SingleInstance()
except:
    playError()
    provisional_app = QApplication()
    icon = QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                              "../assets/icons/favicon.png")))
    provisional_app.setWindowIcon(icon)
    msgBox = QMessageBox()
    msgBox.setWindowTitle("Lost Ark Market Online")
    msgBox.setText(f"Watcher app is already running")
    msgBox.setInformativeText(
        "You should only have 1 app running")
    msgBox.setIcon(QMessageBox.Warning)
    msgBox.exec()
    os._exit(1)
