"""Startup script for the app"""
import logging, sys, yaml
from PyQt5.QtWidgets import QApplication
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
    aboutWidget = AboutWidget.AboutWidget()
    config = yaml.safe_load(loadOrCreateFile("config.yml"))  # Load config
    configForm = ConfigForm.ConfigForm(config)
    uploadWidget = UploadWidget.UploadWidget()

    for widget in [uploadWidget, aboutWidget, configForm]:
        mainWindow.pageStack.addWidget(widget)

    if config is None:
        mainWindow.pageStack.setCurrentIndex(2)
    else:
        mainWindow.pageStack.setCurrentIndex(0)

    mainWindow.showFullScreen()
    sys.exit(app.exec_())  # Without this, the script exits immediately.


if __name__ == "__main__":
    main()
