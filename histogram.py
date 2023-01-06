import numpy as np
from PyQt5.QtWidgets import QMdiSubWindow
from PyQt5.QtWidgets import QTableWidgetItem
from histogram_ui import HistogramSubUI, HistogramListUI


class HistogramSub(QMdiSubWindow, HistogramSubUI):
    def __init__(self, unique_number, img, *args, **kwargs):
        super(HistogramSub, self).__init__(*args, **kwargs)
        self.name = "Histogram of " + img.name
        self.init_ui(self)
        self.is_image = False
        self.unique_number = unique_number
        self.img = img
        self.histogram_list = HistogramList(unique_number+1)
        if img.gray:
            self.button_red.setEnabled(False)
            self.button_green.setEnabled(False)
            self.button_blue.setEnabled(False)
            self.button_all_colors.setEnabled(False)
            self.hist = self.calculate_histogram_gray(img.data)
            self.show_single_channel(self.hist, 'black')
        else:
            self.hist = self.calculate_histogram_color(img.data)
            self.show_all_channel(self.hist)
            self.button_red.pressed.connect(lambda: self.show_single_channel(self.hist, 'r'))
            self.button_blue.pressed.connect(lambda: self.show_single_channel(self.hist, 'b'))
            self.button_green.pressed.connect(lambda: self.show_single_channel(self.hist, 'g'))
            self.button_all_colors.pressed.connect(lambda: self.show_all_channel(self.hist))
        self.button_list.pressed.connect(lambda: self.show_histogram_list(self.hist, img))

    def show_all_channel(self, hist):
        self.histogram_plot.axes.clear()
        for col in "rgb":
            self.histogram_plot.axes.bar(range(256), hist[col], color=col)
        self.histogram_plot.draw()

    def show_single_channel(self, hist, col):
        self.histogram_plot.axes.clear()
        self.histogram_plot.axes.bar(range(256), hist[col], color=col)
        self.histogram_plot.draw()

    def calculate_histogram_gray(self, data):
        my_hist = np.zeros(256)
        for h in range(data.shape[0]):
            for w in range(data.shape[1]):
                current_pixel = data[h, w]
                # print(current_pixel)
                my_hist[current_pixel] += 1

        return {'black': my_hist}

    def calculate_histogram_color(self, data):
        histogram_rgb = [np.zeros(256), np.zeros(256), np.zeros(256)]
        for w in range(data.shape[0]):
            for h in range(data.shape[1]):
                for i in range(data.shape[2]):
                    pixel = data[w][h][i]
                    histogram_rgb[i][pixel] += 1

        return {'b': histogram_rgb[0], 'g': histogram_rgb[1], 'r': histogram_rgb[2]}

    def show_histogram_list(self, hist, img):
        if img.gray:
            self.histogram_list.create_histogram_list(hist['black'], img.name)
        else:
            maximum = [max(i) for i in zip(*hist.values())]
            self.histogram_list.create_histogram_list(maximum, img.name)

        self.histogram_list.show()


class HistogramList(QMdiSubWindow, HistogramListUI):
    def __init__(self, unique_number, *args, **kwargs):
        super(HistogramList, self).__init__(*args, **kwargs)
        self.unique_number = unique_number

    def create_histogram_list(self, hist, img_name):
        self.setWindowTitle("Histogram list of " + img_name)
        self.init_ui(self)
        value_header = self.table_widget.horizontalHeaderItem(0)
        value_header.setText("Nr")
        count_header = self.table_widget.horizontalHeaderItem(1)
        count_header.setText("Count")

        for value, count in enumerate(hist):
            self.table_widget.setItem(value, 0, QTableWidgetItem(str(value)))
            self.table_widget.setItem(value, 1, QTableWidgetItem(str(count)))




