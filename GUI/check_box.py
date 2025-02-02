import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))
        self.check_box=QCheckBox("Do you like the food ?",self)
        self.initUI()
    
    def initUI(self):
        self.check_box.setGeometry(0,0,200,100)
        self.check_box.setStyleSheet("font-size:15px")
        self.check_box.setChecked(False)
        self.check_box.stateChanged.connect(self.checkbox_changed)
        # formula to coonect any functionality whateverthing.signal(may be clicked).connect(slot function or method)
    def checkbox_changed(self,state):
        if state==Qt.Checked:
            print("you like the food")
        else:
            print("You don't like the food")



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

