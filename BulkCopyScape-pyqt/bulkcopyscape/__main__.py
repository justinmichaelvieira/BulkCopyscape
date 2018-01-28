"""Startup script for the app"""
import logging, sys
from PyQt5.QtWidgets import QApplication
import ruamel.yaml as yaml
from .utilities.File import loadOrCreateFile
from .widgets import AboutWidget, ConfigForm, MainWindow, UploadWidget
from . import __version__
# from . import resources_rc  # noqa

app = None
versionString = "Version: " + __version__
logger = logging.getLogger()


def main():
    global app
    app = QApplication(sys.argv)
    app.setOrganizationName("rancorsoft")
    app.setOrganizationDomain("rancorsoft.com")
    app.setApplicationName("BulkCopyScape")
    mainWindow = MainWindow.MainWindow()
    navToUploadScreen = lambda: mainWindow.pageStack.setCurrentIndex(0)
    navToAboutScreen = lambda: mainWindow.pageStack.setCurrentIndex(1)
    navToConfigScreen = lambda: mainWindow.pageStack.setCurrentIndex(2)
    aboutWidget = AboutWidget.AboutWidget(navToUploadScreen)
    config = yaml.safe_load(loadOrCreateFile("config.yml"))  # Load config
    configForm = ConfigForm.ConfigForm(config, navToUploadScreen)
    uploadWidget = UploadWidget.UploadWidget(navToAboutScreen, navToConfigScreen)

    for widget in [uploadWidget, aboutWidget, configForm]:
        mainWindow.pageStack.addWidget(widget)

    if config is None:
        navToConfigScreen()
    else:
        navToUploadScreen()

    mainWindow.showFullScreen()
    sys.exit(app.exec_())  # Without this, the script exits immediately.


if __name__ == "__main__":
    main()
