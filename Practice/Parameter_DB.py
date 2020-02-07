import sqlite3

conn = sqlite3.connect('my_first_db.db')

conn.execute('create table if not exists phones(brand text, version int)')

brand = input('Enter brand of phone: ')
version = input('Enter version of phone (as an integer):')

conn.execute('insert into phones values (?, ?)', (brand, version))

conn.commit()

cur = conn.execute('select * from phones')

for row in cur:
    print(row)
