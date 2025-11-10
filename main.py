from core.books import Book
from core.library import Library

class Main():
    def start_lib_flow():
        pass

if __name__ == "__main__":
    library = Library()

    book_1 = Book("1984", "George Oroville", "1")
    book_2 = Book("A", "A author", "2")
    book_3 = Book("B", "B author", "3")


    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)
    library.print_lib()