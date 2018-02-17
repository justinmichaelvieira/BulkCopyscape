from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QShortcut, QApplication

from .mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.exitShortcut = QShortcut(QKeySequence(Qt.Key_Escape), self)
        self.exitShortcut.activated.connect(lambda: QApplication.quit())
