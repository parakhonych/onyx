import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication
from main_ui import MainWindowUI

class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        """Create a new main window."""

        super().__init__(parent)
        self.init_ui(self)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
