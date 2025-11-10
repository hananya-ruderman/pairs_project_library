
from core.books import Book
from core.user import User

class Library:
    def __init__(self):
        self.list_of_books = []
        self.list_of_users = []
        
    def add_book(self, book: Book):
        self.list_of_books.append(book)
        
    def add_user(self, user: User):
        self.list_of_users.append(user)

    def borrow_book(self, book: Book, user: User):
        if book in self.list_of_books:
            if book.is_available:
                if user in self.list_of_users:
                    book.is_available = False
                    user.barrow_a_book(book)
                    print("borowed succede")
                else:
                    print("user not found")
                    return
            else:
                print("book is not found")
                return
        else:
            print("book not found")
            return
        
    def return_book(self, book: Book, user: User):
        book.is_available = True
        user.borrowed_books.remove(book)
        print("thank you for returning")


               
                    
                    
                


    # def search_in_list(self, item, the_list):
    #     if item in the_list:
    #         return item
    #     else:
    #         print("not in list")
    #         return
                

    def print_lib(self):
        for book in self.list_of_books:
            print(book)
        
    def __str__(self):
        return f"the list of books is {self.list_of_books}"
    

