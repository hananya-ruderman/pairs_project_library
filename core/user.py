

class User:
    def __init__(self, name: str, id: int):
        self.borrowed_times = 0
        self.name = name
        self.id = id 
        self.borrowed_books = []
        self.status = "regular"


    def borrow_a_book(self, book):
        if self.borrowed_times == 10:
            self.status = "gold"
        if self.status == "reguler":
            if len (self.borrowed_books) < 3:
                self.borrowed_books.append(book)
                self.borrowed_times += 1
        if self.status == "gold":
            if len (self.borrowed_books) < 10:
                self.borrowed_books.append(book)


        

    def __str__(self):
        return f"user: {self.name} id: {self.id} borrowed books: {self.borrowed_books}"
    def __repr__(self):
        return f"user: {self.name} id: {self.id} borrowed books: {self.borrowed_books}"