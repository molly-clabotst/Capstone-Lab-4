from model import Record

class SQLJugglerDB():

    def insert(self, name, country, record):
        juggler = Record(name=name, country=country, record=record)
        juggler.save()
        # Confirmation
        print(f"{juggler.name}s' has been saved\n")