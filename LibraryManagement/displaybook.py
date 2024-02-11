
import sqlite3
def displaybook():
    id = int(input("Enter book id: "))
    conn=sqlite3.connect("books.db")
    cursor=conn.cursor()
    cursor.execute("select * from books where book_id=?",(id,))
    book_details=cursor.fetchone()
    if book_details is None:
        print("No records found !")
    else:
        print(book_details)
    

