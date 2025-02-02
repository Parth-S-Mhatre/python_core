import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label=QLabel(self)
        self.time=QTimer(self)
        self.set
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)
        vbox=QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px;"
                                      "color:hsl(132, 85%, 52%);")
        self.setStyleSheet("background-color:black;")
        self.time.timeout.connect(self.update_time)
        self.time.start(1000)
        self.update_time() 
    
    def update_time(self):
        current=QTime().currentTime().toString("hh:mm:ss PM")
        self.time_label.setText(current)



app= QApplication(sys.argv)
clock= Digital_clock()
clock.show()
sys.exit(app.exec_())  # exec means execute 
