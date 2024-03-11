from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as gui
from PyQt6 import QtCore
from PyQt6.QtCore import Qt

import sys
from ColoredWidget import ColoredWidget


class MainWindow(qt.QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Test")
        self.setGeometry(0, 0, 800, 480)

        gameBanner = addColoredBox('blue',sizeX=800, sizeY=310)
        gameBanner.setStyleSheet("margin-left: -1;")
        
        gameIcons = qt.QHBoxLayout()
        gameIconsScrollArea = qt.QScrollArea()
        gameIconsContainerWidget = qt.QWidget()
        
        newsIcon = addColoredBox('green', sizeX=185, sizeY=95)
        gameIcons.addWidget(newsIcon)
        
        for i in range(15):
            gameIcons.addWidget(addColoredBox('red', sizeX=95, sizeY=95))
        
        playerIcons = qt.QHBoxLayout()
        playerIcons.setAlignment(Qt.AlignmentFlag.AlignBottom)
        playerIcons.setSpacing(16)
        
        for i in range(5):
            playerIcons.addWidget(addPlayerIcon(30))
        
        playerIconContainer = qt.QWidget()
        playerIconContainer.setLayout(playerIcons)
        playerIconContainer.setContentsMargins(8,0,0,0)
        
        gameIcons.setAlignment(Qt.AlignmentFlag.AlignLeft)
        gameIcons.setSpacing(28)
        
        gameIconsContainerWidget.setLayout(gameIcons)

        
        gameIconsScrollArea.setWidget(gameIconsContainerWidget)
        
        gameIconsScrollArea.setFrameStyle(0)
        gameIconsScrollArea.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        gameIconsScrollArea.verticalScrollBar().setDisabled(True)        
        gameIconsScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        gameIconsScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        gameIconsScrollArea.setMaximumHeight(100)
        
        mainLayout = qt.QVBoxLayout() 
        
        mainLayout.addWidget(gameBanner)
        mainLayout.addWidget(gameIconsScrollArea)
        mainLayout.addWidget(playerIconContainer)
        
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        mainLayout.setSpacing(0)
        
        centralWidget = qt.QWidget()
        centralWidget.setLayout(mainLayout)
        
        self.setCentralWidget(centralWidget)
   
   
def addColoredBox(*colors, sizeX, sizeY):
    box = ColoredWidget(*colors)
    
    box.setMinimumSize(sizeX, sizeY)
    box.setMaximumSize(sizeX, sizeY)
    
    return box

def addPlayerIcon(size):
    icon = qt.QLabel()
    
    icon.setMinimumSize(size,size)
    icon.setMaximumSize(size,size)
    
    icon.setStyleSheet("QLabel {border: 1px solid black; border-radius: 15px; background: grey;}")
    
    return icon