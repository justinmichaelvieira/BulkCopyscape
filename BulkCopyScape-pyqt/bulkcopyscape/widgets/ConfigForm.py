from PyQt5.QtWidgets import QWidget
from .configform_ui import Ui_Form
from ..utilities.File import saveConfig


class ConfigForm(QWidget, Ui_Form):
    def __init__(self, config, csApi, navBackCb):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        if config is not None:
            self.apiKeyEdit.setText(config["apiKey"])
            self.usernameEdit.setText(config["apiUser"])

        self._config = config
        self._csApi = csApi
        self.saveButton.clicked.connect(lambda: self.saveEnteredValuesAndNav(navBackCb))
        self.cancelButton.clicked.connect(navBackCb)

    def saveEnteredValuesAndNav(self, navCb):
        uname = self.usernameEdit.text()
        apiKey = self.apiKeyEdit.text()
        saveConfig(uname, apiKey)
        self._csApi.uname = uname
        self._csApi.apiKey = apiKey
        navCb()
