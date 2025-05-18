from colorama import Fore

class Library:
    def __init__(self):
        """
        Initializes the Library class with an empty list of books.
        """

        self.users = []
        self.books = []

    def add_user(self, user):
        """
        Adds a user to the library.

        Args:
            user (str): The name of the user to add.
        """
        if user.user_id in self.users:
            print(Fore.RED + "User already exists." + Fore.RESET)
        
        else: 
            self.users[user.user_id] = user
            print(Fore.GREEN + "User added successfully." + Fore.RESET)

    
    def add_book(self, book):
        """
        Adds a book to the library.

        Args:
            book (str): The name of the book to add.
        """
        if book.book_id in self.books:
            print(Fore.RED + "Book already exists." + Fore.RESET)
        
        else: 
            self.books[book.book_id] = book
            print(Fore.GREEN + "Book added successfully." + Fore.RESET)


    def checkout_book(self, user_id, book_id):
        """
        Checks out a book for a user.

        Args:
            user_id (str): The ID of the user checking out the book.
            book_id (str): The ID of the book to check out.
        """

        if user_id in self.users and book_id in self.books:
            book = self.books[book_id]
            if book.checkout(user_id):
                print(Fore.GREEN + f"Book '{book.title}' checked out successfully." + Fore.RESET)
            else:
                print(Fore.RED + f"Book '{book.title}' is already checked out." + Fore.RESET)
        else:
                print(Fore.RED + "User or Book does not exist." + Fore.RESET)

    def return_book(self, user_id, book_id):
        """
        Returns a book for a user.

        Args:
            user_id (str): The ID of the user returning the book.
            book_id (str): The ID of the book to return.
        """
        if user_id in self.users and book_id in self.books:
            book = self.books[book_id]
            if book.return_book(user_id):
                print(Fore.GREEN + f"Book '{book.title}' returned successfully." + Fore.RESET)
            else:
                print(Fore.RED + f"Book '{book.title}' was not checked out by this user." + Fore.RESET)
        else:
                print(Fore.RED + "User or Book does not exist." + Fore.RESET)

    def list_users(self):
        """
        Lists all users in the library.
        """

        if self.users:
            print(Fore.CYAN + "Users:")
            for user in self.users.values():
                print(Fore.CYAN + f"ID: {user.user_id}, Name: {user.name} + Fore.RESET")
        else:
            print(Fore.RED + "No users found." + Fore.RESET)

    def list_books(self):
        """
        Lists all books in the library.
        """
        if self.books:
            print(Fore.CYAN + "Books:")
            for book in self.books.values():
                print(Fore.CYAN + f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}" + Fore.RESET)
        else:
            print(Fore.RED + "No books found." + Fore.RESET)