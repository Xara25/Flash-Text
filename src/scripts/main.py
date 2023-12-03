import sys
from os import path
from PySide6.QtWidgets import QApplication, QWidget
from startup_ui import Ui_Form as Ui_Startup
from memo_ui import Ui_Form as Ui_Memo


def center(widget):
    qr = widget.frameGeometry()
    cp = widget.screen().availableGeometry().center()
    qr.moveCenter(cp)
    widget.move(qr.topLeft())


class Startup(QWidget, Ui_Startup):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        center(self)
        self.dialog = Memo()
        self.pushButton.clicked.connect(self.save)

    def save(self):
        script_path = sys.argv[0]
        file_path = f"{path.dirname(path.dirname(script_path))}/data.txt"

        with open(file_path, "w") as f:
            content = self.plainTextEdit.toPlainText()
            f.write(content)
        print("saving...")
        self.dialog.words = content.split()
        self.hide()
        self.dialog.show()


class Memo(QWidget, Ui_Memo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        center(self)
        self.words = []
        self.i = 0

        self.pushButton.clicked.connect(self.load)

    def load(self):
        if self.i < len(self.words):
            line = " ".join(self.words[: self.i + 1])
            self.textBrowser.setPlainText(
                line
            )  # Use setPlainText to replace the entire content
            self.i += 1


if __name__ == "__main__":
    app = QApplication([])
    window = Startup()
    window.show()
    sys.exit(app.exec())
