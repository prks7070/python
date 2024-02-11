import sqlite3
def returnbook():
    id=int(input("enter book id: "))
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("update books set copies_vailable=copies_vailable+1,issued_to='none',due_date='none' where book_id=?",(id,))
    conn.commit()
    print("book returned successfully !")
    conn.close()
