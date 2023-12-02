import sys
from os import path
from PySide6.QtWidgets import QApplication, QWidget
from startup_ui import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.pushButton.clicked.connect(self.Clicked)

    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def Clicked(self):
        script_path = sys.argv[0]
        file_path = f"{path.dirname(path.dirname(script_path))}/data.txt"

        with open(file_path, "w") as f:
            f.write(self.plainTextEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
