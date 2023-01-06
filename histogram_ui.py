import matplotlib
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import QMetaObject
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = figure.add_subplot(111)
        super(MplCanvas, self).__init__(figure)


class HistogramSubUI:
    def init_ui(self, sub_window):
        self.histogram_plot = MplCanvas(sub_window)
        self.histogram_plot.setObjectName("histogram_plot")

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.layout()
        self.buttons_layout.setObjectName("horizontal_layout")

        self.button_list = QPushButton(self)
        self.button_list.setObjectName("button_list")

        self.button_red = QPushButton(self)
        self.button_red.setObjectName("button_red")
        self.button_red.setAutoDefault(True)

        self.button_green = QPushButton(self)
        self.button_green.setObjectName("button_green")
        self.button_green.setAutoDefault(True)

        self.button_blue = QPushButton(self)
        self.button_blue.setObjectName("button_blue")
        self.button_blue.setAutoDefault(True)

        self.button_all_colors = QPushButton(self)
        self.button_all_colors.setObjectName("button_all_colors")
        self.button_all_colors.setAutoDefault(True)

        self.buttons_layout.addWidget(self.button_all_colors)
        self.buttons_layout.addWidget(self.button_red)
        self.buttons_layout.addWidget(self.button_green)
        self.buttons_layout.addWidget(self.button_blue)
        self.buttons_layout.addWidget(self.button_list)

        self.layout = QVBoxLayout()
        self.layout.setObjectName("layout")

        self.layout.addLayout(self.buttons_layout)
        self.layout.addWidget(self.histogram_plot)

        self.widget = QWidget()
        self.widget.setObjectName("widget")
        self.widget.setLayout(self.layout)

        sub_window.setWidget(self.widget)

        self.__retranslate_ui(sub_window.name)
        QMetaObject.connectSlotsByName(sub_window)

    def __retranslate_ui(self, name):
        _translate = QCoreApplication.translate
        self.setWindowTitle(name)
        self.button_list.setText(_translate(name, "List"))
        self.button_red.setText(_translate(name, "Red"))
        self.button_green.setText(_translate(name, "Green"))
        self.button_blue.setText(_translate(name, "Blue"))
        self.button_all_colors.setText(_translate(name, "All Colors"))

class HistogramListUI:
    def init_ui(self, sub_window):
        sub_window.resize(300, 410)

        self.table_widget = QTableWidget()
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_widget.setColumnCount(2)
        self.table_widget.setRowCount(256)

        for i in range(256):
            self.table_widget.setVerticalHeaderItem(i, QTableWidgetItem())

        item = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)

        item = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)

        sub_window.setWidget(self.table_widget)
