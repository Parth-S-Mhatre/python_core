import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt   # used for alignment 
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\ghost.jpg"))
        label=QLabel("Hello I am parth",self)
        label.setFont(QFont("Times new roman",30))
        label.setGeometry(0,0,500,100)# 0,0 origin will be at top left corner of window
        label.setStyleSheet("color:#4ad970;"
                            "background-color:#0cf5f1;"
                            "font-weight:bold;"
                            "font-style:italic;"
                            "text-decoration:underline;") # hexidecimal color code 
        #label.setAlignment(Qt.AlignTop) # vertically top 
       # label.setAlignment(Qt.AlignBottom) #vertically bottom
       # label.setAlignment(Qt.AlignVCenter)#vertically center
       # label.setAlignment(Qt.AlignRight) #horizantally right
       # label.setAlignment(Qt.AlignHCenter) # h for center 
        #label.setAlignment(Qt.AlignLeft)#horizantally left
        # for combination of both
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # for center and center 
        label.setAlignment(Qt.AlignCenter)

        



app=QApplication(sys.argv)
window=Mainwindow()
window.show()
sys.exit(app.exec_())  # exec means execute 

