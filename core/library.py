
from core.books import Book

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
        
    def add_book(self, book: Book):
        self.list_of_books.append(book)

    def print_lib(self):
        for book in self.list_of_books:
            print(book)
        
    def __str__(self):
        return f"the list of books is {self.list_of_books}"
    

