from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import Qt

from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

QFontDatabase.addApplicationFont("assets/fonts/Nintendo_Switch_UI_Font.ttf")
font = QFont("Nintendo Switch UI")

app.setFont(font)

mainwindow = MainWindow()

mainwindow.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
mainwindow.show()

app.exec()