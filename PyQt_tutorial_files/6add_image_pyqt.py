from pyqt_source import *
# scaling pixmap image to width/height answer:
# https://stackoverflow.com/questions/21802868/python-how-to-resize-raster-image-with-pyqt
class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("image/ui_icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("image/borisut-chamnan-zenozar-1.jpg")
        pixmap = pixmap.scaledToWidth(1000)
        pixmap = pixmap.scaledToHeight(900)
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()



Application = QApplication(sys.argv)
window = Window()
sys.exit(Application .exec())