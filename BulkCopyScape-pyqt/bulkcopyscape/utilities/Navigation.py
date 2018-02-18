from PyQt5.QtGui import QIcon


def setupHeaders(widget, title, callbacksList):
    widget.header.title = title
    widget.navHeader.aboutButton.clicked.connect(callbacksList[0])
    widget.navHeader.aboutButton.setIcon(QIcon(":/icons/about.png"))
    widget.navHeader.resultsButton.clicked.connect(callbacksList[1])
    widget.navHeader.resultsButton.setIcon(QIcon(":/icons/results.png"))
    widget.navHeader.settingsButton.clicked.connect(callbacksList[2])
    widget.navHeader.settingsButton.setIcon(QIcon(":/icons/settings.png"))
    widget.navHeader.checkButton.clicked.connect(callbacksList[3])
    widget.navHeader.checkButton.setIcon(QIcon(":/icons/check.png"))
