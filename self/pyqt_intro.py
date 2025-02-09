import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(720,300,500,500)
        self.setWindowIcon(QIcon("self/download.jpg")) # image not loading
        # label = QLabel("Hello" , self)
        # label.setFont(QFont("Arial" , 20))
        # label.setGeometry(0,0,500,100)
        # label.setStyleSheet("color : red;"
        #                     "background-color : #6fdcf7;"
        #                     "font-weight : bold;"
        #                     "font-style: italic;"
        #                     "text-decoration: underline;")
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #(Qt.AlignCenter) is also done the same work

        label = QLabel(self)
        label.setGeometry(0,0,500,400)
        pixmap = QPixmap("self/pic.jpg") # this picture is also not loading
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width() - label.width())//2,
                          (self.height()-label.height())//2,
                          label.width(),
                          label.height())


def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
    main()