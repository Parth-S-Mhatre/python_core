import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.button=QPushButton("Download now !!",self)
        self.label=QLabel("Flex movie",self)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))
        self.initUI()
    def initUI(self):
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size:20px;")
        self.button.clicked.connect(self.download)    # clicked is as signal 
        self.label.setGeometry(150,300,200,100)
        self.label.setStyleSheet("font-weight:bold;"
                                 "font-size:30px;")
    def download(self):
        print("download started!!")
        self.button.setText("Download started!!")
        self.button.setDisabled(True)
        self.label.setText("Thank you 😉😊")

    



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

