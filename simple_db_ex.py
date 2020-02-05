import sqlite3

conn = sqlite3.connect('first_db.sqlite')
conn.row_factory = sqlite3.Row

conn.execute('create table phones (brand text, version integer)')

conn.execute('insert into phones values ("Android", 5)')
conn.execute('insert into phones values ("Iphone", 6)')

conn.commit()

for row in conn.execute('select * from phones'):
    print(row['brand'])
    print(row['version'])

# conn.execute('drop table phones')

conn.commit()

conn.close()