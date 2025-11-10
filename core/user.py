class User:
    def __init__(self, name: str, id: int, borrowd_books: list[dict]):
        self.name = name
        self.id = id 
        self.borrowed_books = borrowd_books

    def barrow_a_book(self):
        if len (self.borrowed_books) < 3:
            pass
