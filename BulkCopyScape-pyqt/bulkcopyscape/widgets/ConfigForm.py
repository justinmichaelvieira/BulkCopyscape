from PyQt5.QtWidgets import QWidget

from ..utilities.DB import Db
from ..utilities.Navigation import setupHeaders

from .configform_ui import Ui_Form


class ConfigForm(QWidget, Ui_Form):
    def __init__(self, config, csApi, navCallbacks):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._db = Db()

        if config is not None:
            self.apiKeyEdit.setText(config["apiKey"])
            self.usernameEdit.setText(config["apiUser"])

        self._config = config
        self._csApi = csApi
        setupHeaders(self, "Settings", navCallbacks)
        self.saveButton.clicked.connect(self.saveEnteredValues)

    def saveEnteredValues(self):
        uname = self.usernameEdit.text()
        apiKey = self.apiKeyEdit.text()
        self._db.upsertConfig(uname, apiKey)
        self._csApi.uname = uname
        self._csApi.apiKey = apiKey
