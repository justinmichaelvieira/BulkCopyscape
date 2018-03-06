from PyQt5.QtWidgets import QWidget

from .singleresultmatch_ui import Ui_Form


class SingleResultMatch(QWidget, Ui_Form):
    def __init__(self, match, url, title, browserData, parent):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)
        self.matchLbl.setText(match)
        self.urlLbl.setText("<a href=\"{url}\">{url}</a>".format(url=url))
        self.titleLbl.setText(title)
        self.previewBrowser.setText(browserData)
