from PyQt5.QtWidgets import QWidget
from .resultshistory_ui import Ui_Form


class ResultsHistory(QWidget, Ui_Form):
    def __init__(self, backCb):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.backButton.clicked.connect(backCb)
