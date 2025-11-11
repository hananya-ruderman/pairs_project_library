from core.books import Book
from core.user import User
from core.library import Library
from core.user import User
import json


class Main:
    ISBN = 0
    library = Library() 
    def start_lib_flow():
        
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
                Main.library.add_book(user)
                print("congrotulations!!! you are a library member")
            
            if choice == "2":
                new_book = input("enter the book name:  ")
                new_book_author = input("enter the book author:  ")
                Main.ISBN += 1
                book =  Book(new_book, new_book_author, Main.ISBN)
                Main.library.add_book(book)
                print(book)
                Main.write_to_file(book)
               
                print(Main.library.list_of_books)
                
                print("your donation eccepted. thank you")
            
            if choice == "3":
                user_name = input("enter your name:  ")
                book_borrowed = input("enter the book name or author:  ")
                book_ready = Main.library.search_book(book_borrowed)
                Main.library.borrow_book(book_ready[1], user_name)
                
            if choice == "4":
                user_name = input("enter your name:  ")
                returned_book = input("enter the book name or author:  ")
                book_found = Main.library.search_book(returned_book)
                Main.library.borrow_book(book_found[1], user_name)
            
            if choice == "5":
                library_opan = False

    def write_to_file(book):
        with open("library_data.json", "a") as f:
            data = json.dump(book, f, default=str)
        print(data)

        

            




if __name__ == "__main__":
    # main - Main()
    # Main.start_lib_flow()
    # l = Library()
    # print(l.list_of_books)
    # print(l.list_of_users)
    print(Main.write_to_file("fgjh"))
    
   