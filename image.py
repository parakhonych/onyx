import cv2
from PyQt5.QtWidgets import QLabel, QMdiSubWindow
from PyQt5.QtGui import QPixmap, QImage

BYTES_PER_PIXEL_2_BW_FORMAT = {
    1: QImage.Format_Grayscale8,
    2: QImage.Format_Grayscale16,
}

class Image:
    def __init__(self, img_name, img_data, gray, unique_number):
        self.data = img_data
        self.name = img_name
        self.gray = gray
        self.unique_number = unique_number
        self.sub_window = ImageWindow(img_name, img_data, gray, unique_number, scale=1)
        self.is_image = True

class ImageWindow(QMdiSubWindow):
    def __init__(self, img_name, img_data, gray, unique_number, scale, parent=None):
        super().__init__(parent)
        self.data = img_data
        self.name = img_name
        self.gray = gray
        self.unique_number = unique_number
        self.image_label = QLabel()
        self.scale = scale
        self.pixmap = None
        self.setWidget(self.image_label)
        self.setWindowTitle(img_name)
        self.update_window()

    def update_window(self):
        height, width = self.data.shape[:2]

        if self.gray:
            pixel_bytes = self.data.dtype.itemsize
            image = QImage(self.data, width, height, width, BYTES_PER_PIXEL_2_BW_FORMAT[pixel_bytes])
        else:
            #rgb_image = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)
            image = QImage(self.data, width, height, 3 * width, QImage.Format_BGR888)
        self.pixmap = QPixmap(image)
        self.pixmap = self.pixmap.scaled(self.scale * self.pixmap.size())
        self.setFixedSize(self.pixmap.width() + 15, self.pixmap.height() + 35)
        self.image_label.setPixmap(self.pixmap.copy())