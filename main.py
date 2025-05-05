from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QFont, QIcon, QKeyEvent
from PyQt6.QtCore import QSize, Qt
from object import Button, Input
import sys
import re

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.word_list = ["%", "CE", "C", "÷", "7", "8", "9", "x", "4", "5", "6", "-", "1", "2", "3", "+", "↩", "0", ".", "="]
        self.button_list = []
        self.label_text = "0"
        self.setWindowTitle("It's D Calculator")
        self.setFixedWidth(400)
        self.setFixedHeight(500)
        icon = QIcon("Calculator App/images/calculator.png")
        self.setWindowIcon(icon)
        vbox = QVBoxLayout()
        grid = QGridLayout()
        # input field
        self.inupt = Input(self.label_text)
        row = 0
        coloumn = 0
        for i, text in enumerate(self.word_list):
            btn = Button(text)
            grid.addWidget(btn, row, coloumn)
            btn.clicked.connect(lambda _, t=text: self.pressbutton(t))
            self.button_list.append(btn)
            if coloumn == 3:
                row += 1
                coloumn = 0
            else:
                coloumn += 1

        # layout all objects
        vbox.addWidget(self.inupt)
        vbox.addLayout(grid)

        self.setLayout(vbox)

    def keyPressEvent(self, event: QKeyEvent):
        key = event.key()

        if key == Qt.Key.Key_0:
            self.pressbutton("0")
        elif key == Qt.Key.Key_1:
            self.pressbutton("1")
        elif key == Qt.Key.Key_2:
            self.pressbutton("2")
        elif key == Qt.Key.Key_3:
            self.pressbutton("3")
        elif key == Qt.Key.Key_4:
            self.pressbutton("4")
        elif key == Qt.Key.Key_5:
            self.pressbutton("5")
        elif key == Qt.Key.Key_6:
            self.pressbutton("6")
        elif key == Qt.Key.Key_7:
            self.pressbutton("7")
        elif key == Qt.Key.Key_8:
            self.pressbutton("8")
        elif key == Qt.Key.Key_9:
            self.pressbutton("9")
        elif key == Qt.Key.Key_Plus:
            self.pressbutton("+")
        elif key == Qt.Key.Key_Minus:
            self.pressbutton("-")
        elif key == Qt.Key.Key_Slash:
            self.pressbutton("÷")
        elif key == Qt.Key.Key_Asterisk:
            self.pressbutton("x")
        elif key == Qt.Key.Key_Equal or key == Qt.Key.Key_Return or key == Qt.Key.Key_Enter:
            self.pressbutton("=")
        elif key == Qt.Key.Key_Backspace:
            self.pressbutton("↩")
        elif key == Qt.Key.Key_Percent:
            self.pressbutton("%")
        elif key == Qt.Key.Key_C:
            self.pressbutton("C")

    def pressbutton(self, text):
        if text == "C" or text == "CE":
            self.inupt.cleartext()
            self.label_text = "0"

        elif text == "↩":
            self.label_text = self.label_text[:-1]
            if not self.label_text:
                self.label_text = "0"
            self.inupt.changetext(self.label_text)

        elif text == "%":
            # Find the last number and apply % to it
            match = re.search(r"(\d+\.?\d*)$", self.label_text)
            if match:
                number = match.group(1)
                percent = str(float(number) / 100)
                start = match.start(1)
                self.label_text = self.label_text[:start] + percent
                self.inupt.changetext(self.label_text)

        elif text == "=":
            try:
                # Replace symbols with Python operators
                expression = self.label_text.replace("x", "*").replace("÷", "/")
                result = str(eval(expression))
                self.label_text = result
                self.inupt.changetext(self.label_text)
            except Exception:
                self.label_text = "Error"
                self.inupt.changetext(self.label_text)

        elif text in ["x", "+", "-", "÷"]:
            if self.label_text[-1] in ["x", "+", "-", "÷"]:
                # Replace last operator
                self.label_text = self.label_text[:-1] + text
            else:
                self.label_text += text
            self.inupt.changetext(self.label_text)

        else:
            if self.label_text == "0":
                self.label_text = text
            else:
                self.label_text += text
            self.inupt.changetext(self.label_text)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec()