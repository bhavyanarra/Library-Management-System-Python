from Functions import Update_data

# A new class called Books is created with Update_data being the parent class.
# All the methods from the Update_data class are inherited and relevant methods are used in this Books class.
class Books(Update_data):

    def __init__(self):
        super().__init__()
        # a class member is created to store the additions or updates made to the Books table
        self.book_list = []

    # This methods inserts the below values into the Books table in the database.
    # Admin needs to enter these values so that the database can be updated.
    def add_books(self):# Takes ISBN, Title, Author_name, Year, Edition, Loan_status, Loan_date and Loan_user as the inputs
        self.ISBN = input("Please enter the book's ISBN: ")
        self.Title = input("Please enter the book's title: ")
        self.Author_name = input("Please enter the author's name: ")
        self.Year = input("Please enter the year it was published: ")
        self.Edition = input("Please enter the book's edition: ")
        self.Loan_status = input("Please enter the book's status(Available / Loaned): ")
        self.Loan_date = input("If the status is Loaned, please enter the date the book was issued in the format dd-mm-yyyy: ")
        self.Loan_user = input("If the status is Loaned, please enter the username of the borrower: ")

        # The values entered by the admin are stored in a list called new book.
        new_book = [[self.ISBN, self.Title, self.Author_name, self.Year, self.Edition, self.Loan_status, self.Loan_date, self.Loan_user]]
        # The add_book method from the parent class is inherited and the above values are updated in the Books table
        super().add_book('values(?, ?, ?, ?, ?, ?, ?, ?)', new_book[0])
        # the book_list is updated to add in the new book
        self.book_list.append(new_book)


    # This method updates the book details. Not used for issuing the book, but for updating the details of the book
    def update_books(self):# Takes in ISBN, Title, Author_name, Year, Edition, Loan_status, Loan_date and Loan_user as the inputs
        self.ISBN = input("Please enter the book's ISBN: ")
        self.Title = input("Please enter the book's title: ")
        self.Author_name = input("Please enter the author's name: ")
        self.Year = input("Please enter the year it was published: ")
        self.Edition = input("Please enter the book's edition: ")
        self.Loan_status = input("Please enter the book's status(Available / Loaned): ")
        self.Loan_date = input("If the status is Loaned, please enter the date the book was issued in the format dd-mm-yyyy: ")
        self.Loan_user = input("If the status is Loaned, please enter the username of the borrower: ")

        # the inputs provided are stored in a variable and then is passed through the update_book method inherited from the parent class.
        value = [self.ISBN, self.Title, self.Author_name, self.Year, self.Edition, self.Loan_status, self.Loan_date, self.Loan_user]
        super().update_book(value)
        # Updates the book_list for the updated values.
        print(self.book_list.append(value))

# Test codes: Provided as a reference only. Remove # before the code to run this separately.
# This has been added in the main file which runs the application.
# ab = Books()
# Creates a connection to the library database
# ab.create_connection("library.db")

# Adds new books to the database
# ab.add_books()

# Deletes book from the database. This method is inherited from the parent class.
# ab.delete_book()

# Searches for a book based on title. This method is inherited from the parent class.
# ab.search_book()

# Updates book's details in the database.
# ab.update_books()