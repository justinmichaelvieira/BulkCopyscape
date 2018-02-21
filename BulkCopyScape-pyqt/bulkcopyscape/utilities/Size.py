from PyQt5.QtGui import QGuiApplication


def fullScreenSize():
    screen = QGuiApplication.primaryScreen()
    geometry = screen.geometry()
    return geometry
