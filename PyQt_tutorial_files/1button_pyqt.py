from pyqt_source import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "PyQt5 PushButton"
        left = 500
        top = 200
        width = 400
        height = 400
        iconName = "image/ui_icon.png"
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(iconName))
        self.setGeometry(left, top, width, height)
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("Close Application", self)
        #button.move(50,50)
        # button location left -> + = right , - = left, top -> + = bottom, - = top, width -> + = size increase, less
        # size decrease, same for height
        button.setGeometry(QRect(250,350,140,40))
        button.setIcon(QtGui.QIcon("image/close_button.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("&lt;h1&gt;Close the program &lt;h1&gt;")
        button.clicked.connect(self.ButtonAction)

    def ButtonAction(self):
         print("Hello User")
         sys.exit()

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    window_screen = Window()
    sys.exit(Application.exec())
