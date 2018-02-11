from PyQt5.QtWidgets import QWidget, QFileDialog
from .selectfilewidget_ui import Ui_Form


class SelectFileWidget(QWidget, Ui_Form):
    def __init__(self, addWidgetCb):
        super(self.__class__, self).__init__()
        self._addWidgetCb = addWidgetCb
        self.setupUi(self)
        self.selectFileButton.clicked.connect(self.storeFile)

    def storeFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        if fname[0]:
            self._addWidgetCb()
            self.selectedFileEdit.setText(fname[0])
            self.selectedFileEdit.repaint()
