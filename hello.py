"""
    Vanilla example
"""
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello World!")
window.setGeometry(100, 100, 280, 80)

window.move(60, 15)
helloMsg = QLabel('<h1>Hello World!</h1>', parent=window)
helloMsg.move(60, 15)

helloButton = QPushButton("Hello Button", parent=window)
#helloButton.move(0, 0)
window.show() # Paint event init

sys.exit(app.exec_())