from model import Record    
    
class View:

    def __init__(self,view_model):
        self.view_model = view_model

    def make_menu(self):
        choice = ' '
        # menu
        while choice.upper()!= 'Q':
            choice = input('Would you like to...\n1.Add New Record Holder\n2.Search For Record Holder\n3.Show All Records\n4.Update A Record\n5.Delete a Record\nQ.Quit\n\n')
            print()
            if choice == '1':
                add_new_record_holder(self)
            elif choice == '2':
                self.search_for_RH()
            elif choice =='3':
                self.find_all_records()
            elif choice == '4':
                self.update_record()
            elif choice == '5':
                self.delete_record()
            elif choice == 'q':
                print('\nThanks for using the Chainsaw Juggling Record Database\n')
            else:
                print('Please enter a valid menu option, numbers 1-5 or q for quit.\n')

# ADD RECORD
def add_new_record_holder(self):
    name = input('What is the name of daredevil? ')
    country = input('What country does this person come from? ')
    record = input('What is their record for catches? ')
    print()
    # input validation
    if len(name)<2 or len(country)<2 or record.isnumeric==False or len(record)==0:
        print('Please enter full name, country name and a number to input a record.\n')
        return
    # ORM 
    self.insert(name, country, record)
    

# SEARCH
def search_for_RH(self,name = ''):
    # input validation for method reuse
    if len(name)==0:
        name = input('What is the name of the juggler? ')
        # input validation
        while len(name)<2:
            name = input('Please enter the full name of the Chainsaw Juggler\n')    
    # ORM 
    data = Record.select().where(Record.name==name).limit(1)
    # Displaying search results
    if data.exists() == False:
        print(f'\nSorry there was no entry for {name}.\n')
    for dPoint in data:
        print('\n'+str(dPoint)+'\n')

# DISPLAY ALL DATA 
def find_all_records(self):
    # Made this for testing purposes
    data = Record.select()
    if data.exists():
        for record in data:
            print(str(record)+'\n')
    else:
        print('There are no records. Please enter some if you know of them!\n')

# UPDATE
def update_record(self):
    name = input("What is the name of the person whos' record you want to update? ")
    record = input('What is the new number of catches? ')
    print()
    # ORM
    rows_changed = Record.update(record=record).where(Record.name==name).execute()
    # Displaying output
    if rows_changed==0:
        print(f"Sorry {name} isn't in our records. Try entering them instead")
        return
    search_for_RH(name)
    
# DELETE
def delete_record(self):
    # Confirming with user that record should in fact be deleted
    while True:
        name = input("What is the name of the person who's record you want to delete? ")
        search_for_RH(name)
        confirmation = input('Are you sure this is the record you want to delete?(y=yes, n=no) ')
        
        if confirmation.upper() == 'Y':
            break
    # ORM
    rows_deleted = Record.delete().where(Record.name==name).execute()
    # Displaying output 
    if rows_deleted == 0:
        print('There was an error. You might want to check on what is in the records and contact your developer.')
    print(f'The record for {name} was deleted.\n')