import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton 
from PyQt5.QtCore import QTimer,QTime,Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time= QTime(0,0,0,0)
        self.time_label=QLabel("00:00:00.00",self)
        self.start_buttom=QPushButton("Start",self)
        self.stop_buttom=QPushButton("Stop",self)
        self.rest_buttom=QPushButton("Reset",self)
        self.timer=QTimer(self)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Stop watch")
        self.set
        vbox=QVBoxLayout(self)
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)
        hbox=QHBoxLayout(self)
        hbox.addWidget(self.start_buttom)
        hbox.addWidget(self.stop_buttom)
        hbox.addWidget(self.rest_buttom)
        vbox.addLayout(hbox)
        #object name
        self.start_buttom.setObjectName("Start")
        self.stop_buttom.setObjectName("Stop")
        self.rest_buttom.setObjectName("Reset")
        self.setStyleSheet("""
                        QPushButton,QLabel{
                           padding:20px;
                           font-weight:bold;
                           font-family:calibri;
                           }
                        QPushButton{font-size:30px;
                        }
                        QPushButton#Start{
                           background-color:hsl(127, 100%, 64%);
                           }
                        QPushButton#Stop{
                           background-color:hsl(355, 100%, 64%);
                           }
                        QPushButton#Reset{
                           background-color:hsl(30, 100%, 64%);
                           }
                        QPushButton#Start:hover{
                           background-color:hsl(127, 100%, 84%);
                           }
                        QPushButton#Stop:hover{
                           background-color:hsl(355, 100%, 84%);
                           }
                        QPushButton#Reset:hover{
                           background-color:hsl(30, 100%, 84%);
                           }
                             
                        QLabel{font-size:120px;
                           background-color:black;
                           color:white;
                           border-radius:25px;
                           }
                        """)
        self.start_buttom.clicked.connect(self.start)
        self.stop_buttom.clicked.connect(self.stop)
        self.rest_buttom.clicked.connect(self.rest)
        self.timer.timeout.connect(self.update_display)
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def rest(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0) # all are zero because we have to rest it that's why from starting
        self.time_label.setText(self.format_time(self.time))
    def format_time(self,time):
        hours=time.hour()
        mins=time.minute()
        sec=time.second()
        msec=time.msec() // 10
        return f"{hours:02}:{mins:02}:{sec:02}.{msec:02}"
    def update_display(self):
        self.time=self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    

app= QApplication(sys.argv)
stop_watch=Stopwatch() 
stop_watch.show()
sys.exit(app.exec_())