from users.users import User
from books.books import Book
from checkout.checkout import Library
from colorama import init, Fore
import pyfiglet
from importlib import resources


# Initialize colorama
init(autoreset=True)

def print_menu():
    """
    Print the main menu options.

    Displays the main menu options for the library management system.
    1. Add a new user
    2. Add a new book
    3. Checkout a book
    4. Return a book
    5. View all books
    6. View all users
    7. Exit
    """
    print(Fore.CYAN + pyfiglet.figlet_format("Library Management System"))
    print(Fore.YELLOW + "Please choose an option:")
    print(Fore.GREEN + "1. Add a new user")
    print(Fore.GREEN + "2. Add a new book")
    print(Fore.GREEN + "3. Checkout a book")
    print(Fore.GREEN + "4. Return a book")
    print(Fore.GREEN + "5. View all books")
    print(Fore.GREEN + "6. View all users")
    print(Fore.GREEN + "7. Exit")

def main():
    """
    Main function to run the library management system.

    This function initializes the library and starts the main loop for user interaction.
    """
    # Initialize the library
    library = Library()

    while True:
        print_menu()
        choice = input(Fore.GREEN + "Enter your choice: ")

        if choice == '1':
            try:
                user_id = int(input(Fore.GREEN + "Enter user ID: "))
                name = input(Fore.GREEN + "Enter user name: ")
                user = User(user_id, name)
                library.add_user(user)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid user ID.")
        
        elif choice == '2':
            try:
                book_id = int(input(Fore.GREEN + "Enter book ID: "))
                title = input(Fore.GREEN + "Enter book title: ")
                author = input(Fore.GREEN + "Enter book author: ")
                stock = int(input(Fore.GREEN + "Enter book stock: "))
                book = Book(book_id, title, author, stock)
                library.add_book(book)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a valid book ID or stock.")

        elif choice == '3':
            try:
                user_id = int(input(Fore.GREEN + "Enter user ID: "))
                book_id = int(input(Fore.GREEN + "Enter book ID: "))
                library.checkout_book(user_id, book_id)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter valid user ID and book ID.")

        elif choice == '4':
            try:
                user_id = int(input(Fore.GREEN + "Enter user ID: "))
                book_id = int(input(Fore.GREEN + "Enter book ID: "))
                library.return_book(user_id, book_id)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter valid user ID and book ID.")

        elif choice == '5':
            library.list_users()

        elif choice == '6':
            library.list_books()

        elif choice == '7':
            print(Fore.RED + "Exiting the library management system.")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()