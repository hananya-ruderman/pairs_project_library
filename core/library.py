
from core.books import Book
from core.user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
        
    def add_book(self, book: Book):
        self.list_of_books.append(book)
        
    def list_available_books(self):
        list_available_books = []
        for book in self.list_of_books:
            if book.is_available:
                list_available_books.append(book)
        return list_available_books
    
    def search_book(self, word):
        for book in self.list_of_books:
            if word in book:
                return book
            else:
                return 
                
    def add_user(self, user: User):
        self.list_of_users.append(user)

    def print_lib(self):
        for book in self.list_of_books:
            print(book)
        
    def __str__(self):
        return f"the list of books is {self.list_of_books}"