from PyQt5.QtWidgets import QWidget
from .loadingform_ui import Ui_Form


class LoadingForm(QWidget, Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

    def setText(self, text):
        self.label.setText(text)
