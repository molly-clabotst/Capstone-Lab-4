from peewee import *

db = SqliteDatabase('jugglers.sqlite')

class Record(Model):
    name = CharField()
    country = CharField()
    record = CharField()

    class Meta:
        database = db
    
    def __str__(self):
        return f"{self.name} from {self.country}s' record is {self.record}."

db.connect()
db.create_tables([Record])

def main():
    choice = ' '
    while choice.upper()!= 'Q':
        choice = input('Would you like to...\n1.Add New Record Holder\n2.Search For Record Holder\n3.Show All Records\n4.Update A Record\n5.Delete a Record\nQ.Quit\n\n')
        print()
        if choice == '1':
            add_new_record_holder()
        elif choice == '2':
            search_for_RH()
        elif choice =='3':
            find_all_records()
        elif choice == '4':
            update_record()
        # elif choice == 4:
        #     delete_record()
        else:
            print('Please enter a valid menu option, numbers 1-5 or q for quit.\n')

    print('\nThanks for using the Chainsaw Juggling Record Database\n')

def add_new_record_holder():
    name = input('What is the name of daredevil? ')
    country = input('What country does this person come from? ')
    record = input('What is their record for catches? ')
    print()
    if len(name)<2 or len(country)<2 or record.isnumeric==False or len(record)==0:
        print('Please enter full name, country name and a number to input a record.\n')
        return
    juggler = Record(name=name, country=country, record=record)
    juggler.save()
    print(f"{juggler.name}s' has been saved\n")

def search_for_RH(name = ''):
    
    if len(name)==0:
        name = input('What is the name of the juggler? ')
        while len(name)<2:
            name = input('Please enter the full name of the Chainsaw Juggler\n')    
    
    data = Record.select().where(Record.name==name).limit(1)
    if data.exists() == False:
        print(f'\nSorry there was no entry for {name}.\n')

    for dPoint in data:
        print('\n'+str(dPoint)+'\n')
    
def find_all_records():
    data = Record.select()
    if data.exists():
        for record in data:
            print(str(record)+'\n')
    else:
        print('There are no records. Please enter some if you know of them!\n')

def update_record():
    name = input("What is the name of the person whos' record you want to update? ")
    record = input('What is the new number of catches? ')
    print()
    rows_changed = Record.update(record=record).where(Record.name==name).execute()
    if rows_changed==0:
        print(f"Sorry {name} isn't in our records. Try entering them instead")
        return
    search_for_RH(name)
# def delete_record():

if __name__ == '__main__':
    main()