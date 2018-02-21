import xml.etree.cElementTree as etree

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ..utilities.DB import Db
from .SingleResultMatch import SingleResultMatch
from .checkqueryresult_ui import Ui_Form


class CheckQueryResult(QWidget, Ui_Form):
    def __init__(self, resultId, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        fullSize = self.fullScreenSize()
        self.resize(fullSize.width(), fullSize.height())
        self.closeBtn.clicked.connect(lambda: self.hide())
        row = Db().getResultById(resultId)
        self.fnameLbl.setText(row['filename'])
        subbed = row['result'][2:].replace('\\t', '').replace('\\n', '').replace('&', '&#038;').strip('\'')
        root = etree.fromstring(subbed)
        self.numWordsLbl.setText(root.find('querywords').text)
        self.numMatchesLbl.setText(root.find('count').text)
        self._srmList = []
        self._scrollLayout = QVBoxLayout(self)
        self.resultsScrollContents.setLayout(self._scrollLayout)
        for result in root.findall('result'):
            newSrm = SingleResultMatch(result.find('index').text, result.find('url').text,
                                       result.find('title').text, result.find('htmlsnippet').text,
                                       self.resultsScrollContents)
            self._scrollLayout.addWidget(newSrm)
            self._srmList.append(newSrm)

    def fullScreenSize(self):
        screen = QGuiApplication.primaryScreen()
        geometry = screen.geometry()
        return geometry
