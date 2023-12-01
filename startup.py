import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPlainTextEdit,
    QWidget,
    QVBoxLayout,
    QPushButton,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

app = QApplication([])


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Flash Text")
        self.resize(750, 512)
        self.center()

        self.label = QLabel("Enter Text", self)
        self.label.setFont(QFont("Arial", 30))
        self.input = QPlainTextEdit(self)
        self.button = QPushButton("Send", self)
        self.button.setFixedSize(125, 50)
        self.button.setFont(QFont("Arial", 20))
        self.button.clicked.connect(self.Clicked)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(
            self.label,
            alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter,
        )
        self.vbox.addWidget(self.input)
        self.vbox.addWidget(
            self.button,
            alignment=Qt.AlignmentFlag.AlignRight,
        )
        self.setLayout(self.vbox)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Clicked(self):
        print(self.input.toPlainText())


if __name__ == "__main__":
    window = Window()
    window.show()
    sys.exit(app.exec())
