from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from ..utilities.DB import Db
from .SelectFileWidget import SelectFileWidget
from .LoadingForm import LoadingForm
from .uploadwidget_ui import Ui_Form


class UploadWidget(QWidget, Ui_Form):
    def __init__(self, csApi, aboutFormCb, configFormCb):
        super(self.__class__, self).__init__()
        self._csApi = csApi
        self._selectFileWidgets = []
        self._numFiles = 0
        self._loadingForm = LoadingForm()
        self.setupUi(self)
        self._scrollLayout = QVBoxLayout()
        self.scrollAreaWidgetContents.setLayout(self._scrollLayout)
        self.titleHeader.title = "Check Files"
        self.navHeader.aboutButton.clicked.connect(aboutFormCb)
        self.navHeader.aboutButton.setIcon(QIcon(":/icons/about.png"))
        self.navHeader.settingsButton.clicked.connect(configFormCb)
        self.navHeader.settingsButton.setIcon(QIcon(":/icons/settings.png"))
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
        self._loadingForm.hide()

    @pyqtSlot(int)
    def updateProcessed(self, numProcessed):
        self._loadingForm.setText(
            "Uploading Files - {filesDone} of {numFiles} complete.".format(
                filesDone=numProcessed, numFiles=self._numFiles))


class CheckThread(QThread):
    completed = pyqtSignal()
    updateProcessed = pyqtSignal(int)

    def __init__(self, files, csApi, updatedCb, completedCb):
        QThread.__init__(self)
        self._db = Db()
        self._files = files
        self._csApi = csApi
        self.completed.connect(completedCb)
        self.updateProcessed.connect(updatedCb)
        self.start()

    def checkAndSaveResults(self, fname):
        with open(fname, "r") as f:
            contents = f.read()
            response = self._csApi.copyscape_api_text_search_internet(contents, "UTF-8")
            self._db.insertResult(str(response))

    def run(self):
        filesDone = 0
        for fname in self._files:
            self.checkAndSaveResults(fname)
            filesDone += 1
            self.updateProcessed.emit(filesDone)
            self.sleep(1)
        self.completed.emit()
