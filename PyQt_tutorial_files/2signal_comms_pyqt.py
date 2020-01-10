from pyqt_source import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = 'PyQt5 Signal & Slots'
        left = 500
        top = 200
        width = 300
        height = 250
        iconName = 'image/ui_icon.png'
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left,top, width, height)
        self.CreateButton()
        self.show()

# from line 4-16 is just the init/dna of the program to start & position the info

    def CreateButton(self):
        button = QPushButton("Close Application", self)
        button.setGeometry(QRect(90, 100, 130, 40))
        button.setIcon(QtGui.QIcon("image/close_button.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.clicked.connect(self.ButtonAction)

    def ButtonAction(self):
        sys.exit()

# basic info, the button from def createbutton will create a 'signal' to the program to close the program by connecting
# to the function buttonaction which closes the program due to having sys.exit()

Application = QApplication(sys.argv)
window_screen = Window()
sys.exit(Application.exec())
