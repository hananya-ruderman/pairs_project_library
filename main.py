from core.books import Book
from core.user import User
from core.library import Library
from core.user import User

class Main:
    def start_lib_flow():
        pass

if __name__ == "__main__":
    library = Library()
    # users = User()

    book_1 = Book("1984", "George Oroville", "1")
    book_2 = Book("A", "A author", "2")
    book_3 = Book("B", "B author", "3")
    user_1 = User("moshe", 1234)
    print(type(book_1))
   
    library.add_user(user_1)
    book_1.is_available = True
    book_2.is_available = True
    book_3.is_available = False
    

    library.add_book(book_1)
    library.add_book(book_2)
    library.add_book(book_3)
    # library.print_lib()
    # library.borrow_book(book_1, user_1 )
    # library.return_book(book_1, user_1)
    a = [(1,2), (3,4)]
    # print(library.search_book("2"))
    print(library.list_of_books)
    my_list = library.list_of_books
    my_dict = dict(my_list)
    print(my_dict)