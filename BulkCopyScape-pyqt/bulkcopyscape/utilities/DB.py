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

    def saveConfig(self, apiUser, apiKey):
        table = self.db['config']
        table.delete()
        table.insert(dict(apiUser=apiUser, apiKey=apiKey))

    def getConfig(self):
        return self.db['config'].find_one(id=1)
