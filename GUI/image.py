import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap   # for adding,loading image 
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        label=QLabel(self) # self refers to the windows i.e parent Qwindow
        label.setGeometry(0,0,250,250)
        pixmap=QPixmap("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
          # windows geometry - label geometry 
        label.setGeometry((self.width()-label.width()) // 2,
                          (self.height()-label.height()) // 2     # dividing by 2 means we are round-off to height or width
                          ,label.width(),
                          label.height())



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 