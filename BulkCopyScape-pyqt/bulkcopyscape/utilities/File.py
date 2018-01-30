"""Handles files, file types and file transforms"""
import ruamel.yaml as yaml
from PyQt5.QtCore import QFile, QTextStream


def loadOrCreateFile(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        saveConfig("", "")
        f = open(filename, 'r')
    return f


def saveConfig(apiUser, apiKey):
    with open("config.yml", 'w') as f:
        yaml.safe_dump({"apiUser": apiUser, "apiKey": apiKey}, f)


def getFileContents(filename):
    file = QFile(filename)
    file.open(QFile.Text | QFile.ReadOnly)
    st = QTextStream(file)
    return st.readAll()
