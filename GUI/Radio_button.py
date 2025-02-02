import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QRadioButton,QButtonGroup
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))
        self.radio1=QRadioButton("VISA",self)
        self.radio2=QRadioButton("Mastercard",self)
        self.radio3=QRadioButton("Gift card",self)
        self.radio4=QRadioButton("In-store",self)
        self.radio5=QRadioButton("Online",self)
        self.group_button1=QButtonGroup(self)
        self.group_button2=QButtonGroup(self)

        self.initUI()
    
    def initUI(self):
        self.radio1.setGeometry(0,0,500,100)
        self.radio2.setGeometry(0,50,450,100)
        self.radio3.setGeometry(0,100,400,100)
        self.radio4.setGeometry(0,150,450,100)
        self.radio5.setGeometry(0,200,400,100)
        self.setStyleSheet("QRadioButton{""font-size: 40px;"
                           "font-family:Arial;"
                           "padding: 10px;""}")
        self.group_button1.addButton(self.radio1)
        self.group_button1.addButton(self.radio2)
        self.group_button1.addButton(self.radio3)
        self.group_button2.addButton(self.radio4)
        self.group_button2.addButton(self.radio5)
        self.radio1.toggled.connect(self.radio_button_change)
        self.radio2.toggled.connect(self.radio_button_change)
        self.radio3.toggled.connect(self.radio_button_change)
        self.radio4.toggled.connect(self.radio_button_change)
        self.radio5.toggled.connect(self.radio_button_change)


    
    def radio_button_change(self):
        radio_button=self.sender() # which one sends the signal 
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected ")
        pass









app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

