import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from main_ui import MainWindowUI
from image import Image

class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        """Create a new main window."""

        super().__init__(parent)
        self.init_ui(self)
        self.active_image = None
        self.images = dict()
        self.unique_number = 0

        # Define File menu actions
        self.action_open_gray.triggered.connect(self.open_gray)
        self.action_open_color.triggered.connect(self.open_color)

    def open_gray(self):
        files_paths, _ = QFileDialog.getOpenFileNames(self, "Open file", "", "Image files (*.bmp *.jpeg *.jpg *.bmp "
                                                                             "*.png *.tiff *.tif);;")
        if not files_paths:
            return
        for file_path in files_paths:
            self.__open_file(file_path, True)

    def open_color(self):
        files_paths, _ = QFileDialog.getOpenFileNames(self, "Open file", "", "Image files (*.bmp *.jpeg *.jpg *.bmp "
                                                                             "*.png *.tiff *.tif);;")
        if not files_paths:
            return
        for file_path in files_paths:
            self.__open_file(file_path, False)

    def __open_file(self, file_path, gray):
        img_name = file_path.split("/")[-1]
        if gray:
            img_data = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        else:
            img_data = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
        self.unique_number = self.unique_number + 1
        image = Image(img_name, img_data, gray, self.unique_number)
        self.images[self.unique_number] = image
        self.mdi.addSubWindow(image.sub_window)
        image.sub_window.show()


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
