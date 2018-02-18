from PyQt5.QtWidgets import QWidget

from ..utilities.Navigation import setupHeaders

from .aboutwidget_ui import Ui_Form


class AboutWidget(QWidget, Ui_Form):
    def __init__(self, navCallbacks):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        setupHeaders(self, "About", navCallbacks)
