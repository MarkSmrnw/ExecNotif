import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

from general.printing import debugPrint


# Loads the designer file in this folder! (I hope)
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        uic.loadUi("ui/main.ui", self)  # type: ignore (Type-Error because uic is not typed correctly.)

    def buttonClick(self):
        debugPrint("A button has been clicked!")


def start():
    """Starts the GUI"""

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
