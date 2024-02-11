
import sqlite3
#bk=book.book()

def add_book():
    #bk=book.book()
    bname=input("Book name: ")
    
    bid=int(input("Book id: "))
    
    authorname=input("Author: ")
    
    count=int(input("No. of copies: "))
    
    issuerid=input("Issuer Id: ")
    
    duedate=input("Due Date: ")
    
    conn=sqlite3.connect("books.db")
    conn.execute(''' insert into books(book_id,book_name,author,copies_vailable,issued_to,due_date) values(?,?,?,?,?,?)''',(bid,bname,authorname,count,issuerid,duedate))
    conn.commit()
    conn.close()
    print("Book record added successfully !")
    
    
