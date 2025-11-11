from core.books import Book
from core.user import User
from core.library import Library
from core.user import User

   

l = Library()
book = Book("today", "you", 2345)

print(l.add_book(book))
print(l.list_of_books)
for book in l.list_of_books:
    print(book)
    print(type(book))
    # a = l.search_book("asd")
    # print(a[1])

    
    
        # users = User()

   
   
    # print(type(book_1))
   
    # library.add_user(user_1)
    # book_1.is_available = True
    # book_2.is_available = True
    # book_3.is_available = False
    

    # library.add_book(book_1)
    # library.add_book(book_2)
    # library.add_book(book_3)
    # # print(library.list_available_books())
    # # library.print_lib()
    # # library.borrow_book(book_1, user_1 )
    # # library.return_book(book_1, user_1)
    # a = [(1,2), (3,4)]
    # print(library.search_book("2"))
    # # print(library.list_of_books)
    # my_list = library.list_of_books
    # # my_dict = dict(my_list)
    # # print(my_dict)
