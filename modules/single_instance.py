
import os
import sys
import tempfile
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from modules.sound import playError

class SingleInstanceException(BaseException):
    pass

class SingleInstance(object):
    def __init__(self, flavor_id="", lockfile=""):
        self.initialized = False
        if lockfile:
            self.lockfile = lockfile
        else:
            basename = os.path.splitext(os.path.abspath(sys.argv[0]))[0].replace(
                "/", "-").replace(":", "").replace("\\", "-") + '-%s' % flavor_id + '.lock'
            self.lockfile = os.path.normpath(
                tempfile.gettempdir() + '/' + basename)    
            try:
                if os.path.exists(self.lockfile):
                    os.unlink(self.lockfile)
                self.fd = os.open(
                    self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            except OSError:
                type, e, tb = sys.exc_info()
                if e.errno == 13:
                    raise SingleInstanceException()
                print(e.errno)
                raise
        self.initialized = True

    def __del__(self):
        if not self.initialized:
            return
        try:
            if hasattr(self, 'fd'):
                os.close(self.fd)
                os.unlink(self.lockfile)
        except Exception as e:
            print("Unloggable error: %s" % e)
            sys.exit(-1)


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
