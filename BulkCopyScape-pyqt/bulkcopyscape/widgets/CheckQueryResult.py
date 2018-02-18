from PyQt5.QtWidgets import QWidget
from .checkqueryresult_ui import Ui_Form


class CheckQueryResult(QWidget, Ui_Form):
    def __init__(self, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
