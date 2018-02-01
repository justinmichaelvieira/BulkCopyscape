"""Startup script for the app"""
# Todo: Either tab nav on top of app, or "fake tab nav" with buttons/widget
# Todo: Resize widgets to screen on size change
# Todo: Result history and display
# Todo: 'Please wait' modal popup while sending to BCS
import logging
import sys
from PyQt5.QtWidgets import QApplication
import ruamel.yaml as yaml
from .utilities.File import loadOrCreateFile, getFileContents
from .utilities.CopyscapeApi import CopyscapeApi
from .widgets import AboutWidget, ConfigForm, MainWindow, UploadWidget
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
    aboutWidget = AboutWidget.AboutWidget(navToUploadScreen)
    config = yaml.safe_load(loadOrCreateFile(configFile))  # Load config
    configForm = ConfigForm.ConfigForm(config, csApi, navToUploadScreen)
    uploadWidget = UploadWidget.UploadWidget(csApi, navToAboutScreen, navToConfigScreen)

    for widget in [uploadWidget, aboutWidget, configForm]:
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
