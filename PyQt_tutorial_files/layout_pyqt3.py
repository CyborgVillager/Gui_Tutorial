from pyqt_source import *

# program will be using a class called QHBoxLayout that will make its widgets line up horizontal
# also be importing QDialog/QVBoxLayout & QGroupBox

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title ='Layout HBox Gui'
        self.top = 200
        self.left = 200
        self.width = 400
        self.height = 500
        self.iconName = 'image/ui_icon.png'
        self.CreateButton()
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
        self.groupBox = QGroupBox("What Is Your Favorite Programming Language ?")
        hboxLayout = QHBoxLayout()
        self.button = QPushButton("Python", self)
        self.button.setIcon(QtGui.QIcon("image/python.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        hboxLayout.addWidget(self.button)
        self.button2 = QPushButton("C+", self)
        self.button2.setIcon(QtGui.QIcon("image/c_plus.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        hboxLayout.addWidget(self.button2)
        self.button3 = QPushButton("Html", self)
        self.button3.setIcon(QtGui.QIcon("image/html5.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setMinimumHeight(40)
        hboxLayout.addWidget(self.button3)
        self.groupBox.setLayout(hboxLayout)


    def CreateButton(self):
        button = QPushButton("Close Application", self)
        button.setGeometry(QRect(140, 300, 130, 40))
        button.setIcon(QtGui.QIcon("image/close_button.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.clicked.connect(self.ButtonAction)

    def ButtonAction(self):
        sys.exit()

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    window_screen = Window()
    sys.exit(Application.exec())