"""Startup script for the app"""
import logging
import sys
import ruamel.yaml as yaml

from PyQt5.QtWidgets import QApplication

from .utilities.File import loadOrCreateFile, getFileContents, resource_path
from .utilities.CopyscapeApi import CopyscapeApi
from .widgets import AboutWidget, ConfigForm, MainWindow, ResultsHistory, UploadWidget
from . import __version__
from . import resources_rc  # noqa

app = None
versionString = "Version: " + __version__
logger = logging.getLogger()
configFile = resource_path("config.yml")
apiKeyEntry = "apiKey"
apiUserEntry = "apiUser"


def main():
    global app
    app = QApplication(sys.argv)
    app.setOrganizationName("rancorsoft")
    app.setOrganizationDomain("rancorsoft.com")
    app.setApplicationName("BulkCopyScape")
    app.setStyleSheet(getFileContents(":/css/style.css"))
    csApi = CopyscapeApi()
    mainWindow = MainWindow.MainWindow()
    navToUploadScreen = lambda: mainWindow.pageStack.setCurrentIndex(0)
    navToAboutScreen = lambda: mainWindow.pageStack.setCurrentIndex(1)
    navToConfigScreen = lambda: mainWindow.pageStack.setCurrentIndex(2)
    navToResultsScreen = lambda: mainWindow.pageStack.setCurrentIndex(3)
    navCallbacks = [navToAboutScreen, navToResultsScreen, navToConfigScreen, navToUploadScreen]
    aboutWidget = AboutWidget.AboutWidget(navCallbacks)
    resultsWidget = ResultsHistory.ResultsHistory(navCallbacks)
    config = yaml.safe_load(loadOrCreateFile(configFile))  # Load config
    configForm = ConfigForm.ConfigForm(config, csApi, navCallbacks)
    uploadWidget = UploadWidget.UploadWidget(csApi, navCallbacks, resultsWidget.populateResults)

    for widget in [uploadWidget, aboutWidget, configForm, resultsWidget]:
        mainWindow.pageStack.addWidget(widget)

    if config:
        navToUploadScreen()
        csApi.apiKey = config[apiKeyEntry]
        csApi.uname = config[apiUserEntry]
    else:
        navToConfigScreen()

    mainWindow.showFullScreen()
    sys.exit(app.exec_())  # Without this, the script exits immediately.


if __name__ == "__main__":
    main()
