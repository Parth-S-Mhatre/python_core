import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QPushButton
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))
        self.text_box=QLineEdit(self)
        self.submit=QPushButton("Submit!!",self)
        self.initUI()
    def initUI(self):
        self.text_box.setGeometry(10,10,200,40)
        self.submit.setGeometry(220,10,100,40)
        self.text_box.setStyleSheet("font-size:25px")
        self.submit.setStyleSheet("font-size:22px")
        self.text_box.setPlaceholderText("Enter the name")
        self.submit.clicked.connect(self.submited)
        

    def submited(self):
        text=self.text_box.text()
        print(f"hello {text}")



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

