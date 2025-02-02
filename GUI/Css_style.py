import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHOST 1.0")
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")
        self.initUI()
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)

        # Set object names for the buttons
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Set the stylesheet
        self.setStyleSheet("""
            QPushButton {
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;    
                margin: 25px;
                border: 3px solid;
                border-radius: 15px;
            }
            QPushButton#button1 {
                background-color: hsl(0, 100%, 64%);
            }
            QPushButton#button2 {
                background-color: hsl(239, 100%, 64%);
            }
            QPushButton#button3 {
                background-color: hsl(132, 100%, 64%);
            }
            QPushButton#button1:hover {
                background-color: hsl(0, 100%, 84%);
            }
            QPushButton#button2:hover {
                background-color: hsl(239, 100%, 84%);
            }
            QPushButton#button3:hover {
                background-color: hsl(132, 100%, 84%);
            }
        """)

# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())  # exec means execute

""" padding means space between text and border margin means space between widget and button border radius means all the corner are rounded

"""