"""Startup script for the app"""
# Todo: Result history and display, columns = datetime (default sort), filename, Results button
# Todo: Should be updating the modal text after each check, and enabling a "close" button at the end
# Todo: Back button top nav bar for About widget, remove current btn
import logging
import sys
from PyQt5.QtWidgets import QApplication
import ruamel.yaml as yaml
from .utilities.File import loadOrCreateFile, getFileContents
from .utilities.CopyscapeApi import CopyscapeApi
from .widgets import AboutWidget, ConfigForm, MainWindow, ResultsHistory, UploadWidget
from . import __version__
from . import resources_rc  # noqa

app = None
versionString = "Version: " + __version__
logger = logging.getLogger()
configFile = "config.yml"
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
    aboutWidget = AboutWidget.AboutWidget(navToUploadScreen)
    resultsWidget = ResultsHistory.ResultsHistory(navToUploadScreen)
    config = yaml.safe_load(loadOrCreateFile(configFile))  # Load config
    configForm = ConfigForm.ConfigForm(config, csApi, navToUploadScreen)
    uploadWidget = UploadWidget.UploadWidget(csApi, navToAboutScreen, navToResultsScreen,  navToConfigScreen)

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
