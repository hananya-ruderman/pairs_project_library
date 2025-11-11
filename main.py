from core.books import Book
from core.user import User
from core.library import Library
from core.user import User


class Main:
    ISBN = 0
    def start_lib_flow():
        library = Library() 
        library_opan = True
        while library_opan:

            print("\n===============start menu====================")
            print()
            print("1) not a member? sign up  ")
            print("2) want to donate a book?  ")
            print("3) would you like to borrow a book?  ")
            print("4) would you like to return a book?  ")
            print("5) exit  ")
            choice = input("please enter the number of your choice: ")
            if choice == "1":
                new_user = input("enter your name:  ")
                new_user_id = input("enter your id:  ")
                user =  User(new_user, new_user_id)
                library.add_user(user)
            
            if choice == "2":
                new_book = input("enter the book name:  ")
                new_book_author = input("enter the book author:  ")
                Main.ISBN += 1
                book =  Book(new_book, new_book_author, Main.ISBN)
                library.add_book(book)
            
            if choice == "3":
                user_name = input("enter your name:  ")
                book_borrowed = input("enter the book name or author:  ")
                book_ready = library.search_book(book_borrowed)
                library.borrow_book(book_ready[1], user_name)
                
            if choice == "4":
                user_name = input("enter your name:  ")
                returned_book = input("enter the book name or author:  ")
                book_found = library.search_book(returned_book)
                library.borrow_book(book_found[1], user_name)
            if choice == "5":
                library_opan = False

            




if __name__ == "__main__":
    # main - Main()
    Main.start_lib_flow()
  
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
