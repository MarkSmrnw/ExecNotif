import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from general.printing import debugPrint


# Loads the designer file in this folder! (I hope)
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.ui = uic.loadUi("ui/main.ui")  # type: ignore (Type-Error because uic is not typed correctly.)
        self.setWindowTitle("ExecNotif")
        self.setGeometry(0, 0, 500, 250)
        self.setCentralWidget(self.ui)

        self.pushButton: QPushButton = self.ui.pushButton  # type: ignore
        self.pushButton.clicked.connect(self.buttonClick)

    def buttonClick(self):
        debugPrint("A button has been clicked!")


def start():
    """Starts the GUI"""

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
