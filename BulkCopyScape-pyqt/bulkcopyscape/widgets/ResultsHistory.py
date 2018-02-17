from PyQt5.QtWidgets import QWidget
from ..utilities.DB import Db
from .resultshistory_ui import Ui_Form


class ResultsHistory(QWidget, Ui_Form):
    def __init__(self, backCb):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._db = Db()
        self.backButton.clicked.connect(backCb)
        self.populateResults()

    def populateResults(self):
        self.resultsList.clear()
        for res in self._db.getResults():
            fn = str(res['filename'])
            ts = str(res['timestamp'])
            self.resultsList.addItem("{0} - {1}".format(fn, ts))
