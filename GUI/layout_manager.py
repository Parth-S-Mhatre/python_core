import sys                                         # for vertical box and also horizontal
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))
        self.initUI()
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        label1=QLabel("#1",self)
        label2=QLabel("#2",self)
        label3=QLabel("#3",self)
        label4=QLabel("#4",self)
        label5=QLabel("#5",self)

        label1.setStyleSheet("background-color:blue;")
        label2.setStyleSheet("background-color:red;")
        label3.setStyleSheet("background-color:green;")
        label4.setStyleSheet("background-color:yellow;")
        label5.setStyleSheet("background-color:purple;")
        # for horizontal just replace V with H
        """"
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        central_widget.setLayout(vbox)
        """
        grid=QGridLayout()   # matrix of 3X2 is created
                            # r c
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,0,2)
        grid.addWidget(label4,1,0)
        grid.addWidget(label5,1,1)
        central_widget.setLayout(grid)
        



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

