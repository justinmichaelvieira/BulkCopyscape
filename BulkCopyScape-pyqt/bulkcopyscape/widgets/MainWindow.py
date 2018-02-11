from PyQt5.QtWidgets import QMainWindow
from .mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
