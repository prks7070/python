import sqlite3
conn=sqlite3.connect("books.db")

conn.execute(''' insert into books values (002,'War and Peace','Leo Tolstoy',5,'S002','25-12-2023')''')
        
conn.commit()
conn.close()