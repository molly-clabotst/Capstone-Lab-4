from peewee import *


# Database
db = SqliteDatabase('jugglers.sqlite')

# Model
class Record(Model):
    name = CharField()
    country = CharField()
    record = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return f"{self.name} from {self.country}s' record is {self.record}."

# Connect and create db
db.connect()
db.create_tables([Record])