from pyqt_source import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt Tut Window'
        self.top = 200
        self.left = 500
        self.width = 500
        self.height = 600
        self.InitWindow()

    def InitWindow(self):
        #self.setWindowIcon(QtGui.QIcon("image/borisut-chamnan-zenozar-1.jpg")) # picture too big
        self.setWindowIcon(QtGui.QIcon("image/ui_icon.png")) # This icon looks a bit more better than an all out picture
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


Application = QApplication(sys.argv)
window = Window()
sys.exit(Application.exec())