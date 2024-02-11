import sqlite3
from datetime import datetime, timedelta
from displaybook import *
def issuebook():
    id=int(input("enter book id : "))
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from books where book_id=?",(id,))
    book_details=cur.fetchone()
    if book_details is None or book_details[3]==0:
        print("No records found ! , book cannot be issued")
    else:
        issuer_id=input("enter user id: ")
        current_date = datetime.now().date()
        due_date = current_date + timedelta(weeks=1)
        dd=due_date.strftime('%d-%m-%Y')
        cur.execute("update books set copies_vailable=copies_vailable-1,issued_to=?,due_date=? where book_id=?",(issuer_id,dd,id))
        conn.commit()
        print("book issued successfully !")
        
    conn.close()


