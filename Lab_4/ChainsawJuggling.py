from peewee import *

db = SqliteDatabase('jugglers.sqlite')

class Records(Model):
    name = CharField()
    country = CharField()
    record = IntegerField()

    class Meta:
        database = db
    
    def __str__(self):
        return f"{self.name} from {self.country}s' record is {self.record}."

db.connect()
db.create_tables([Records])

def main():
    choice = ' '
    while choice.upper()!= 'Q':
        choice = input('Would you like to...\n1.Add New Record Holder\n2.Search For Record Holder\n3.Update A Record\n4.Delete a Record\nQ.Quit\n\n')
        print()
        if choice == '1':
            add_new_record_holder()
        # elif choice == 2:
        #     search_for_RH()
        # elif choice == 3:
        #     update_record()
        # elif choice == 4:
        #     delete_record()

    print('\nThanks for using the Chainsaw Juggling Record Database\n')

def add_new_record_holder():
    name = input('What is the name of daredevil? ')
    country = input('What country does this person come from? ')
    record = input('What is their record for catches? ')
    print()
    if len(name)<2 or len(country)<4 or record.isnumeric==False or len(record)==0:
        print('Please enter full name, country name and a number to input a record.\n')
        return
    juggler = Records(name=name, country=country, record=record)
    juggler.save()
    print(f"{juggler.name}s' has been saved")

# def search_for_RH():


# def update_record():

# def delete_record():

if __name__ == '__main__':
    main()