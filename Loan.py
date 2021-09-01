from Functions import Update_data
from datetime import datetime
import timedelta

# Created a separate class for Loan.
class Loan(Update_data):

    def __init__(self):
        super().__init__()

    # The below function displays books that are available in the library
    def view_books(self):
        super().search_book()

    # Issue_books method issues the book to a particular member
    def issue_books(self):
        # For the username, the membership type is first taken and the count for the no. of books in their account is taken.
        # Using if else statements, if the membership type is basic and he has 2 books already in his account,
        # the application will give an error stating that he already has 2 books.
        # Similarly, the same process is repeated for 4 books for premium membership.
        # If the number of books is below the limit, then the application will issue the book to the user.
        self.Username = input("Please enter the username of the member you wish to check: ")
        membership = super().check_membership(self.Username)
        count = super().count_book_(self.Username)
        if membership == "Basic" and count == 2:
            print("This user already has two books in his account")
        elif membership == "Premium" and count == 4:
            print("This user already has four books in his account")
        else:
            print("This user can borrow additional books.")
            # To issue the book to the user, the application requests the user to search for the book available
            super().search_book()
            # The ISBN, issue date and the username of the member are then updated in the database.
            self.ISBN = input("Please copy the ISBN of the book that the member wishes to borrow and enter here: ")
            self.Loan_date = input("Please enter the issue date: ")
            value = [self.ISBN, self.Loan_date, self.Username]
            super().update_issue(value)

    # This code returns the book to the library and also calculates fine if the no. of days exceed 60.
    def return_book(self):
        self.ISBN = input("Please enter the ISBN of the book that is being returned: ")
        self.return_date = str(input("Please enter the date this book is returned: "))
        issue_date = super().issue_date(self.ISBN)
        # As the date format here are as string, they are first converted to date format and then the difference is
        # calculated.
        diff = (timedelta.Timedelta((datetime.strptime(self.return_date, "%d-%m-%Y")).date() - issue_date)).days
        # Below code displays the fine if the book is returned after 60 days
        if diff > 60:
            print("Book is returned after 60 days, please collect a fine of 10 pounds!")
        else:
            print("Book is returned within 60 days.")
        # Below code updates the status of the book back to available, removes loan_date and Loan_user against that
        # book in the database.
        super().update_status(self.ISBN)


cd = Loan()
# cd.view_books()
# cd.issue_books()
# cd.books_user("xyz@yahoo.com")
# cd.user_books()
# cd.return_book()

