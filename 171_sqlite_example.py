import sqlite3
conn = sqlite3.connect('my_database')
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
query = """ -- sqlite queries are strings; comments use
"--"
create table address -- create a table named "address"
( -- begin creating a record
name varchar, -- create a field called "name", with type
"varchar"
street varchar,
city varchar
) -- end of this record
""" # end of query
addresses = [
('Pet Shops Ltd', '123 Main St', 'Notlob'),
('Similar Pet Shops Ltd', '321 First St', 'Bolton'),
]
for addr in addresses:
	cursor.execute("insert into address values (?, ?, ?)", addr)
cursor.execute("select name from address")
print cursor.fetchall()
cursor.execute("select * from address where city='Bolton'")
print cursor.fetchall()
