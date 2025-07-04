class Book:
    def __init__(self, title, author, year, stock):
        """
        initialize a Book instance.

        :param title: Title of the book
        :param author: Author of the book
        :param year: Year of publication
        :param stock: Number of copies available
     
        :return: None
        """
        self.title = title
        self.author = author
        self.year = year
        self.stock = stock
        self.checked_out_users = []

    
    def checkout(self, user_id):
        """
        Check out a book to a user.

        This method checks if the book is available in stock and allows a user to check it out.
        If the book is already checked out by the maximum number of users, it returns False.
        If the book is available, it adds the user ID to the list of checked out users and returns True.

        :param user_id: ID of the user checking out the book
        
        :return: Bool indicating success or failure
        """

        if self.stock > len(self.checked_out_users):
            self.checked_out_users.append(user_id)
            return True
        else:
            return False
        
    def return_book(self, user_id):
        """
        Return a book from a user.

        :param user_id: ID of the user returning the book
        
        :return: Bool indicating success or failure
        """
        if user_id in self.checked_out_users:
            self.checked_out_users.remove(user_id)
            return True
        else:
            return False