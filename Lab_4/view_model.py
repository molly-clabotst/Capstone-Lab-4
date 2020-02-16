from model import Record

class ViewModel:

    def __init__(self, db):
        self.db = db
    
    def insert(self, name, country, record):
        self.db.insert(self, name, country, record)