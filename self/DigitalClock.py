import sys 
from PyQt5.QtWidgets import QApplication, QWidget , QLabel , QVBoxLayout
from PyQt5.QtCore import QTimer , QTime , Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.TimeLabel = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(720,400,600,150)

        vbox = QVBoxLayout()

        vbox.addWidget(self.TimeLabel)
        self.setLayout(vbox)


        self.TimeLabel.setAlignment(Qt.AlignCenter)
        self.TimeLabel.setStyleSheet("font-size: 150px;"
                                     "font-family: Arial;"
                                     "color: hsl(111,100%,50%);")
        
        self.setStyleSheet("background-color : black;")

        self.timer.timeout.connect(self.Update_time)
        self.timer.start(1000)

        self.Update_time()
    
    def Update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.TimeLabel.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())
