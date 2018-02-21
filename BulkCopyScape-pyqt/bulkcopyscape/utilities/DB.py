import dataset
import datetime


class Db(object):
    def __init__(self):
        self.db = dataset.connect('sqlite:///bcs.db')

    def insertResult(self, fileName, resultText):
        table = self.db['results']
        table.insert(dict(filename=fileName, result=resultText, timestamp=datetime.datetime.now()))

    def getResults(self):
        return self.db['results'].all()

    def getResultById(self, resultId):
        return self.db['results'].find_one(id=resultId)
