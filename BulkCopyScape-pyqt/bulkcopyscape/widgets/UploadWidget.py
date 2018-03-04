import html
import os

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QVBoxLayout

from ..utilities.DB import Db
from ..utilities.Navigation import setupHeaders
from ..utilities.Layout import clearAllWidgets
from .SelectFileWidget import SelectFileWidget
from .LoadingForm import LoadingForm
from .uploadwidget_ui import Ui_Form


class UploadWidget(QWidget, Ui_Form):
    def __init__(self, csApi, navCallbacks, popResHistCb):
        super(self.__class__, self).__init__()
        self._db = Db()
        self._csApi = csApi
        self._selectFileWidgets = []
        self._numFiles = 0
        self._loadingForm = LoadingForm()
        self._refreshHistory = popResHistCb
        self.setupUi(self)
        self._scrollLayout = QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self._scrollLayout)
        setupHeaders(self, "Check Files", navCallbacks)
        self.runTestsButton.clicked.connect(self.runTests)
        self.addSelectFileWidget()

    def addIfEmpty(self, text):
        if text == "":
            self.addSelectFileWidget()

    def addSelectFileWidget(self):
        sfWidget = SelectFileWidget(lambda: self.addIfEmpty(sfWidget.selectedFileEdit.text()))
        self._scrollLayout.addWidget(sfWidget)
        self._selectFileWidgets.append(sfWidget)

    def runTests(self):
        self._loadingForm.showMaximized()
        filesList = []
        for sfw in self._selectFileWidgets:
            fname = sfw.selectedFileEdit.text()
            if fname is not "":
                filesList.append(fname)
        self._numFiles = len(filesList)
        self._loadingForm.setText("Uploading Files - 0 of {numFiles} complete.".format(numFiles=self._numFiles))
        CheckThread(filesList, self._csApi, self.updateProcessed, self.completed)

    @pyqtSlot()
    def completed(self):
        clearAllWidgets(self._scrollLayout)
        self._selectFileWidgets = []
        self._numFiles = 0
        self.addSelectFileWidget()
        self._refreshHistory()
        self._loadingForm.hide()

    @pyqtSlot(str, str, int)
    def updateProcessed(self, fname, response, numProcessed):
        self._loadingForm.setText(
            "Uploading Files - {filesDone} of {numFiles} complete.".format(
                filesDone=numProcessed, numFiles=self._numFiles))
        self._db.insertResult(os.path.basename(fname), html.unescape(response))


class CheckThread(QThread):
    completed = pyqtSignal()
    updateProcessed = pyqtSignal(str, str, int)

    def __init__(self, files, csApi, updatedCb, completedCb):
        QThread.__init__(self)
        self._files = files
        self._csApi = csApi
        self.completed.connect(completedCb)
        self.updateProcessed.connect(updatedCb)
        self.start()

    def checkAndSaveResults(self, fname):
        with open(fname, "r") as f:
            contents = f.read()
            return self._csApi.copyscape_api_text_search_internet(contents, "UTF-8")

    def run(self):
        filesDone = 0
        for fname in self._files:
            response = self.checkAndSaveResults(fname)
            filesDone += 1
            self.updateProcessed.emit(fname, str(response), filesDone)
            self.sleep(1)
        self.completed.emit()
