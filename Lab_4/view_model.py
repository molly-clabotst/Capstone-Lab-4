from model import Record

class ViewModel:

    # def __init__(self, db):
    #     self.db = db
    
    def insert(self, name, country, record):
        juggler = Record(name=name, country=country, record=record)
        juggler.save()
        # Confirmation
        print(f"{juggler.name}s' has been saved\n")