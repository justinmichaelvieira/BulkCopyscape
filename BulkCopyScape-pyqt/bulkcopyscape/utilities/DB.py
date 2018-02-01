import dataset
import datetime


class Db(object):
    def __init__(self):
        self.db = dataset.connect('sqlite:///bcs.db')

    def insertResult(self, resultText):
        table = self.db['results']
        table.insert(dict(result=resultText, timestamp=datetime.datetime.now()))
