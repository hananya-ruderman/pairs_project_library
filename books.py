class Books:
    def __init__(self, title, author, ISBN, is_available):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.is_available = True
        
    def __str__(self):
        print(f"The book: {self.title}, from {self.author}, {self.is_available} is_available")
        