import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMediaPlayer, QVideoWidget
from PyQt5.QtMultimedia import QMediaContent

class VideoButtonApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Video on Button')
        self.setGeometry(100, 100, 640, 480)

        # Create the player
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget(self)
        self.player.setVideoOutput(videoWidget)

        # Create button
        self.button = QPushButton('Play Video', self)
        self.button.clicked.connect(self.play_video)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(videoWidget)

        self.setLayout(layout)

    def play_video(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("C:\\Users\\parth\\OneDrive\\Desktop\\parth\\icons8-sent.gif")))
        self.player.play()

app = QApplication(sys.argv)
window = VideoButtonApp()
window.show()
sys.exit(app.exec_())
