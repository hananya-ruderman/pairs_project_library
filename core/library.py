
from books import Book
from user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
        
    def add_book(self, book: Book):
        book = tuple(book,)
        self.list_of_books.append(book)
        
    def add_user(self, user: User):
        self.list_of_users.append(user)

    def borrow_book(self, book: Book, user: User):
        if self.search_book(book):
            if book.is_available:
                if user in self.list_of_users:
                    book.is_available = False
                    user.barrow_a_book(book)
                    print("borowed succede")
                else:
                    print("user not found")
                    return
            else:
                print("book is not found")
                return
        else:
            print("book not found")
            return
        
    def return_book(self, book: Book, user: User):
        book.is_available = True
        user.borrowed_books.remove(book)
        print("thank you for returning")


    def list_available_books(self):
        list_available_books = []
        for book in self.list_of_books:
            if book.is_available:
                list_available_books.append(book)
        return list_available_books
    
    def search_book(self, word):
        for book in self.list_of_books:
            if word in book:
                return True
            else:
                return False
   
    def print_lib(self):
        for book in self.list_of_books:
            print(book)
        
    def __str__(self):
        return f"the list of books is {self.list_of_books}"