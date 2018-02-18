from PyQt5.QtWidgets import QWidget
from .singleresultmatch_ui import Ui_Form


class SingleResultMatch(QWidget, Ui_Form):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
