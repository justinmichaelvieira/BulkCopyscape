# TODO: Widget that shows all Results from one query and query stats (QueryResults)
# and Widget that represents one result match (SingleResultMatch) for repeating in a single QueryResults
from PyQt5.QtWidgets import QWidget

from ..utilities.DB import Db
from ..utilities.Navigation import setupHeaders

from .resultshistory_ui import Ui_Form


class ResultsHistory(QWidget, Ui_Form):
    def __init__(self, navCallbacks):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._db = Db()
        self.populateResults()
        setupHeaders(self, "Results", navCallbacks)

    def populateResults(self):
        self.resultsList.clear()
        for res in self._db.getResults():
            fn = str(res['filename'])
            ts = str(res['timestamp'])
            self.resultsList.addItem("{0} - {1}".format(fn, ts))
