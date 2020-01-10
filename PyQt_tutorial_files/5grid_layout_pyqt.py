from pyqt_source import *

# this program will make a continaer that will let the buttons/widgets show in a
# grid like pattern
# pyqt colors tutorial : https://pythonspot.com/pyqt5-colors/

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Grid Layout Gui'
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = 'image/ui_icon.png'
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()


    def CreateLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Programming Language")
        gridLayout = QGridLayout()
        self.button = QPushButton("Python", self)
        self.button.setIcon(QtGui.QIcon("image/python.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(50)
        gridLayout.addWidget(self.button, 0,0)

        self.button2 = QPushButton("C++", self)
        self.button2.setIcon(QtGui.QIcon("image/c_plus.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(50)
        gridLayout.addWidget(self.button2, 0,1)

        self.button3 = QPushButton("Html", self)
        self.button3.setIcon(QtGui.QIcon("image/html5.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setMinimumHeight(50)
        gridLayout.addWidget(self.button3,1,0)

        self.button4 = QPushButton("Random pic", self)
        self.button4.setIcon(QtGui.QIcon("image/borisut-chamnan-zenozar-1.jpg"))
        self.button4.setIconSize(QtCore.QSize(40, 40))
        self.button4.setMinimumHeight(50)
        gridLayout.addWidget(self.button4, 1, 1)
        self.groupBox.setLayout(gridLayout)

        self.button5 = QPushButton('Close Applicaton', self)
        self.button5.setIcon(QtGui.QIcon('image/close_button.png'))
        self.button5.setIconSize(QtCore.QSize(30,30))
        self.button5.setMinimumHeight(40)
        gridLayout.addWidget(self.button5, 2, 1)
        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())