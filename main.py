import cv2
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from main_ui import MainWindowUI
from image import Image
from histogram import HistogramSub

class MainWindow(QMainWindow, MainWindowUI):
    def __init__(self, parent=None):
        """Create a new main window."""

        super().__init__(parent)
        self.init_ui(self)
        self.active_image = None
        self.images = dict()
        self.unique_number = 0

        self.mdi.subWindowActivated.connect(self.update_active_window)

        # Define File menu actions
        self.action_open_gray.triggered.connect(self.open_gray)
        self.action_open_color.triggered.connect(self.open_color)
        self.action_save.triggered.connect(self.save_image)

        # Define Windows menu actions
        self.action_duplicate.triggered.connect(self.image_duplication)
        self.action_cascade.triggered.connect(self.mdi.cascadeSubWindows)
        self.action_zoom_50.triggered.connect(lambda: self.zoom_in(0.5))
        self.action_zoom_75.triggered.connect(lambda: self.zoom_in(0.75))
        self.action_zoom_80.triggered.connect(lambda: self.zoom_in(0.8))
        self.action_zoom_90.triggered.connect(lambda: self.zoom_in(0.9))
        self.action_zoom_100.triggered.connect(lambda: self.zoom_in(1))
        self.action_zoom_150.triggered.connect(lambda: self.zoom_in(1.5))
        self.action_zoom_200.triggered.connect(lambda: self.zoom_in(2))
        self.action_zoom_plus.triggered.connect(lambda: self.zoom_in(0.1))
        self.action_zoom_minus.triggered.connect(lambda: self.zoom_in(-0.1))

        # Define Functions menu actions
        self.action_histogram.triggered.connect(self.show_histogram)

        # Define Info menu actions
        self.action_info.triggered.connect(self.show_info)

    def show_info(self) -> None:
        info = """
        <a href="https://www.flaticon.com/authors/smashicons" title="retail icons">Icons created by Smashicons - Flaticon</a>
        """

        QMessageBox.information(self, "About", info)

    def __add_window(self, img_name, img_data, gray):
        self.unique_number = self.unique_number + 1
        image = Image(img_name, img_data, gray, self.unique_number)
        self.images[self.unique_number] = image
        self.mdi.addSubWindow(image.sub_window)
        image.sub_window.show()

    def zoom_in(self, scale):
        if scale < 0.2:
            self.active_image.sub_window.scale += scale
        else:
            self.active_image.sub_window.scale = scale
        self.active_image.sub_window.update_window()

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
        self.__add_window(img_name, img_data, gray)

    def update_active_window(self, sub):
        if sub is not None:
            if sub.unique_number in self.images:
                self.active_image = self.images.get(sub.unique_number)
    def save_image(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save file", self.active_image.name, "All Files (*);;")
        if not file_path:
            return
        cv2.imwrite(file_path, self.active_image.data)

    def image_duplication(self):
        self.__add_window("duplication " + self.active_image.name, self.active_image.data, self.active_image.gray)

    def show_histogram(self):
        self.unique_number = self.unique_number + 1
        hist = HistogramSub(self.unique_number, self.active_image)
        self.mdi.addSubWindow(hist)

        self.unique_number = self.unique_number + 1
        self.mdi.addSubWindow(hist.histogram_list)

        hist.show()


if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
