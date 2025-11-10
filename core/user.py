

class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id 
        self.borrowed_books = []


    def barrow_a_book(self, book):
        if len (self.borrowed_books) < 3:
            self.borrowed_books.append(book)

    def __str__(self):
        return f"user: {self.name} id: {self.id} borrowed books: {self.borrowed_books}"
