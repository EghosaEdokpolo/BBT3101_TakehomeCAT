class Book:
    def __init__(self, title, author):
        self.ititle = title
        self.iauthor = author
        self.is_borrowed = False

    def set_borrowed(self):
        self.is_borrowed = True

    def set_returned(self):
        self.is_borrowed = False

class Library_member:
    def __init__(self, name, member_id):
        self.iname = name
        self.imember_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed == False:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print("book is successfully borrowed")
        else:
            print("book is already borrowed, sorry")

    def return_book(self, book):
        if book.is_borrowed == True:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print("book is successfully returned")
        else:
            print("book has not been borrowed yet")

    def list_borrbooks(self):
        for book in self.borrowed_books:
            print(f"\n{book.ititle} by {book.iauthor}")

#execution
book1 = Book("the pigmy princess", "micheal bobley")
book2 = Book("the great gatsby", "leonard davinci")

#ineractive code
inp_name = input("enter name : ")
inp_id = input("enter member id : ")


lmemb = Library_member(inp_name, inp_id)

option = "waiting"
while option != "exit":
    option = input("enter 'borrow', 'return', 'list', 'exit'")

    if option == "borrow":
        book_name = input("enter the name of the book you want to borrow: ")
        if book_name == book1.ititle:
            lmemb.borrow_book(book1)
            option = "waiting"
        elif book_name == book2.ititle:
            lmemb.borrow_book(book2)
            option = "waiting"
        else: 
            print("invalid book")
            option = "waiting"

    elif option == "return":
        book_name = input("enter the name of the book you want to return: ")
        if book_name == book1.ititle:
            lmemb.return_book(book1)
            option = "waiting"
        elif book_name == book2.ititle:
            lmemb.return_book(book2)
            option = "waiting"
        else: 
            print("invalid request")
            option = "waiting"

    elif option == "list":
        lmemb.list_borrbooks()
        option = "waiting"

    elif option == "exit":
        option = "exit"
    else:
        option = "waiting"