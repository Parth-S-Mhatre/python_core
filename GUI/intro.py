import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

