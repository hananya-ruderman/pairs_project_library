class Book():
    def __init__(self,title,author, isbn):
        self.title = title
        self.author = author
        self.ISBN = isbn
        self.is_available = True
        
    def __str__(self):
        return f"The book: {self.title} from {self.author} ISBN :{self.ISBN} available: {self.is_available}"
        
    def __repr__(self):
        return f"The book: {self.title} from {self.author} ISBN :{self.ISBN} available: {self.is_available}"
        

        