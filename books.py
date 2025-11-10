class Book:
    ISBN = 1000
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.ISBN = Book.ISBN
        Book.ISBN += 1
        self.is_available = True
        
    def __str__(self):
        return f"The book: {self.title}, from {self.author},ISBN :{self.ISBN} {self.is_available} is_available"
        
class Library:
    def __init__(self):
        self.library = []
        
    def add_book(self, title , author):
        new_Book = Book(title,author)
        self.library.append(new_Book)

    def print_lib(self):
        for book in self.library:
            print(book)
        
        
        
library = Library()

names =[["brachot","rav"],["gitin","raba"]]
for input in names:
    library.add_book(input[0],input[1])


print("============= Books ==============")
library.print_lib()