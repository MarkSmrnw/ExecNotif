import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

from general.printing import debugPrint

mainApp: QApplication | None = None
mainWindow: QMainWindow | None = None


# basic template for a basic window.
class _MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temp")
        self.resize(500, 500)

        label = QLabel("Label Label Label Label Label Label Label")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


def startMainUi():

    global mainWindow, mainApp

    if mainWindow is None:
        debugPrint("Starting window...")

        mainApp = QApplication(sys.argv)
        mainWindow = _MainWindow()
        mainWindow.show()
        sys.exit(mainApp.exec())
