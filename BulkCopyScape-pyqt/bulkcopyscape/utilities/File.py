"""Handles files, file types and file transforms"""
import os
import sys

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
    with open(resource_path("config.yml"), 'w') as f:
        yaml.safe_dump({"apiUser": apiUser, "apiKey": apiKey}, f)


def getFileContents(filename):
    file = QFile(filename)
    file.open(QFile.Text | QFile.ReadOnly)
    st = QTextStream(file)
    return st.readAll()


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)