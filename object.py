from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QSpacerItem, QSizePolicy,QLabel
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import QSize, Qt
import sys


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.text = text
        self.setFixedHeight(50)
        if self.text == "=":
            self.setStyleSheet("background-color: lightblue;")

        

class Input(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.text = text
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setFixedSize(380, 100)
        self.setStyleSheet("font-size: 30pt;")

    def cleartext(self):
        self.clear()
        self.changetext("0")

    def changetext(self, text):
        self.text = text
        self.setText(self.text)
