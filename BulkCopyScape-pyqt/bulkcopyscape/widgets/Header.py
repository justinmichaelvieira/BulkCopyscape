from PyQt5.QtWidgets import QWidget
from .header_ui import Ui_Form


class Header(QWidget, Ui_Form):
    @property
    def title(self):
        return self.titleLabel.text()

    @title.setter
    def title(self, val):
        self.titleLabel.setText(val)

    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
