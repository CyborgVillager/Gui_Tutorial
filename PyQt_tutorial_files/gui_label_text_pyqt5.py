from pyqt_source import *

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Gui Label With Text"
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 500
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("image/ui_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()

        label0 = QLabel("Hello User")
        label0.setFont(QtGui.QFont("Sanserif", 15))
        label0.setStyleSheet('color:red')
        vbox.addWidget(label0)

        label1 = QLabel("Welcome to your dashboard x,y,z")
        label1.setFont(QtGui.QFont("Sanserif", 25))
        label1.setStyleSheet('color:black')
        vbox.addWidget(label1)
        self.setLayout(vbox)
        self.show()




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())