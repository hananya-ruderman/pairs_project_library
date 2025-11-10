from core.books import Book
from core.user import User
from core.library import Library

class Main():
    def start_lib_flow():
        pass

if __name__ == "__main__":
    library = Library()
    # users = User()

    book_1 = Book("1984", "George Oroville", "1")
    book_2 = Book("A", "A author", "2")
    book_3 = Book("B", "B author", "3")
    book_1.is_available = True
    book_2.is_available = True
    book_3.is_available = False
    

    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)
    library.print_lib()
    x = library.list_available_books()
    print(x)