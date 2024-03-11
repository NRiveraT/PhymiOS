from PyQt6 import QtWidgets as qt
from PyQt6.QtGui import QPalette, QColor


class ColoredWidget (qt.QWidget):
    
    def __init__(self, color):
        super(ColoredWidget, self).__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))

        self.setPalette(palette)        