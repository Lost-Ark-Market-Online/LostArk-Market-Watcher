from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget


class DraggableWindow(QWidget):
    dragging = False

    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

    def mousePressEvent(self, event):
        self.dragging = True
        self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.dragging = False
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.parent().move(self.parent().x() + delta.x(), self.parent().y() + delta.y())
            self.oldPos = event.globalPos()
