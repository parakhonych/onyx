from PyQt5 import QtCore, QtWidgets


class MainWindowUI:
    def init_ui(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)

        self.mdi = QtWidgets.QMdiArea()
        self.mdi.setObjectName("mdi_area")
        main_window.setCentralWidget(self.mdi)

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menu_bar.setObjectName("menu_bar")

        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_file")

        self.menu_windows = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menu_windows")


        self.menu_functions = QtWidgets.QMenu(self.menu_bar)
        self.menu_functions.setObjectName("menu_function")

        main_window.setMenuBar(self.menu_bar)

        # File menu
        self.action_open_gray = QtWidgets.QAction(main_window)
        self.action_open_gray.setObjectName("action_open_gray")
        self.action_open_color = QtWidgets.QAction(main_window)
        self.action_open_color.setObjectName("action_open_color")
        self.action_save = QtWidgets.QAction(main_window)
        self.action_save.setObjectName("action_save")

        self.menu_file.addAction(self.action_open_gray)
        self.menu_file.addAction(self.action_open_color)
        self.menu_file.addAction(self.action_save)

        # Windows menu
        self.action_duplicate = QtWidgets.QAction(main_window)
        self.action_duplicate.setObjectName("action_duplicate")

        self.menu_windows.addAction(self.action_duplicate)

        # Function menu
        self.action_histogram = QtWidgets.QAction(main_window)
        self.action_histogram.setObjectName("action_histogram")

        self.menu_functions.addAction(self.action_histogram)


        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_windows.menuAction())
        self.menu_bar.addAction(self.menu_functions.menuAction())

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate

        main_window.setWindowTitle(_translate("main_window", "Onyx"))

        self.menu_file.setTitle(_translate("main_window", "File"))
        self.action_open_gray.setText(_translate("main_window", "Open(Gray)"))
        self.action_open_color.setText(_translate("main_window", "Open(Color)"))
        self.action_save.setText(_translate("main_window", "Save"))

        self.menu_windows.setTitle(_translate("main_window", "Windows"))
        self.action_duplicate.setText(_translate("main_window", "Duplicate"))

        self.menu_functions.setTitle(_translate("main_window", "Functions"))
        self.action_histogram.setText(_translate("main_window", "Histogram"))

