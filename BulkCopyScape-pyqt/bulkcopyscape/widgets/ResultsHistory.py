from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtCore import Qt, pyqtSlot

from ..utilities.DB import Db
from ..utilities.Navigation import setupHeaders

from .CheckQueryResult import CheckQueryResult
from .resultshistory_ui import Ui_Form


class ResultsHistory(QWidget, Ui_Form):
    def __init__(self, navCallbacks):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._db = Db()
        self._singleResultMatch = None
        self.populateResults()
        setupHeaders(self, "Results", navCallbacks)

    @pyqtSlot(QListWidgetItem)
    def on_resultsList_itemClicked(self, item):
        self._checkQueryResult = CheckQueryResult(item.data(Qt.UserRole), self)
        self._checkQueryResult.show()

    def populateResults(self):
        self.resultsList.clear()
        for res in self._db.getResults():
            id = str(res['id'])
            fn = str(res['filename'])
            ts = str(res['timestamp'])
            qlwi = QListWidgetItem()
            qlwi.setData(Qt.UserRole, id)
            qlwi.setText("{0} - {1}".format(fn, ts))
            self.resultsList.addItem(qlwi)
