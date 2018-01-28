"""Handles files, file types and file transforms"""


def loadOrCreateFile(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        f = open(filename, 'w')
    return f
