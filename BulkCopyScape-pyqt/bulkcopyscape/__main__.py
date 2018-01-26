"""Startup script for the app"""
import logging
import sys
import yaml
from PyQt5.QtWidgets import QApplication
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
    # with open('config.yml') as f:
    #    config = yaml.safe_load(f)  # Load config
    sys.exit(app.exec_())  # Without this, the script exits immediately.


if __name__ == "__main__":
    main()
