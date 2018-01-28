"""Handles files, file types and file transforms"""
import ruamel.yaml as yaml


def loadOrCreateFile(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        f = open(filename, 'w')
    return f


def saveConfig(apiUser, apiKey):
    with open("config.yml", 'w') as f:
        yaml.safe_dump({"apiUser": apiUser, "apiKey": apiKey}, f)
