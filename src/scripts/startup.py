import sys
from PySide6.QtWidgets import QApplication, QWidget
from startup_ui import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Clicked(self):
        with open("data.txt", "w") as f:
            f.write(self.input.toPlainText())


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
