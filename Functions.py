import sqlite3
from datetime import datetime


def create_connection( db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except KeyError as e:
        print(e)
    return conn

# Connecting to Library database
conn = create_connection(db_file="library.db")
conn.execute("PRAGMA foreign_keys = 1")
# Creating a cursor for the database
c = conn.cursor()


# Creating a parent class that adds data, updates and deletes the data in the database.
# This class contains all SQL operations and has all input variables where the user can provide the values

class Update_data(object):

    # The first method is to create a connection to the library database
    @classmethod
    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except KeyError as e:
            print(e)
        return conn

    @classmethod
    # add_book method inserts new values into the book table.
    def add_book(cls, columns, new_values):
        a = 'INSERT INTO Books '
        col = columns
        try:
            # adds values into the Books table in the library database
            c.execute(a + col, new_values)
            # Saves the database after adding the new values
            conn.commit()
            print(f'New book details has been added to the table')
        # capture KeyError
        except KeyError as e:
            print(e, 'KeyError occurred below results may not be valid')

    # update_book method updates the book details in the database for that particular ISBN
    @classmethod
    def update_book(cls, value):
        try:
            c.execute('''UPDATE Books SET Title = (?), Author_name = (?), Year = (?), Edition = (?), Loan_status = (?), Loan_date = (?), Loan_user = (?) WHERE ISBN == (?)''',
        (value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[0]))
            conn.commit()
            print(f'Updated book details in the table')
        except KeyError as e:
            print(e)

    # delete_book method deletes the book details for a particular ISBN.
    # As this is a console based application, ISBN is requested from the user.
    @classmethod
    def delete_book(cls):
        ISBN = input("Please enter the ISBN of the book you want to delete: ")
        try:
            c.execute("DELETE FROM Books WHERE ISBN == '%s'" % ISBN)
            conn.commit()
            print("Book deleted from the database")
        except KeyError as e:
            print(e)

    # Search_book method searches the value given in the input and searches for that value in the title.
    # As we need to get the title that contains the value, we use %title% to search in the database.
    @classmethod
    def search_book(cls):
        Title = input("Please enter the name of the book: ")
        try:
            Title = ('%'+Title+'%')
            c.execute("SELECT * FROM Books WHERE Loan_status = 'Available' AND Title LIKE ?", [Title])
            book = c.fetchall()
            conn.commit()
            # If there is no book with that title, the database returns an empty list than displaying an error.
            # As such, if it returns an empty list, then it prints the below statement as error.
            # If not, then the list of books are displayed on the screen.
            if book == []:
                print("There are no books available in the library with this title")
            else:
                print("Below are the books are available in the library with this title")
                for row in book:
                    print(row)
        except KeyError as e:
            print(e)

    # add_member method inserts new values into the member table.
    @classmethod
    def add_member(cls, columns, member_values):
        a = 'INSERT INTO Members '
        col = columns
        try:
            c.execute(a + col, member_values)
            conn.commit()
            print(f'New member details has been added to the table')
        # capture KeyError
        except KeyError as e:
            print(e)

    # update_member methods updates the value of that member for which the username is given
    @classmethod
    def update_member(cls, member_value):
        try:
            c.execute(
                '''UPDATE Members SET Password = (?), Name = (?), Address = (?), Contact_number = (?), Membership_type = (?), Is_admin = (?) WHERE Username == (?)''',
                (member_value[1], member_value[2], member_value[3], member_value[4], member_value[5], member_value[6], member_value[0]))
            conn.commit()
            print(f'Updated member details in the table')
        except KeyError as e:
            print(e)

    # Delete_member method deletes the row for the given username
    @classmethod
    def delete_member(cls):
        Username = input("Please enter the username of the member you wish to delete: ")
        try:
            c.execute("DELETE FROM Members WHERE Username == '%s'" % Username)
            conn.commit()
            print("Member deleted from the database")
        except KeyError as e:
            print(e)

    # Search_member method searches for that input in the username.
    # Any value in the username similar to the input returns those member's details
    @classmethod
    def search_member(cls):
        Username = input("Please enter the username of  the member you wish to search: ")
        try:
            Username = ('%' + Username + '%')
            c.execute("SELECT * FROM Members WHERE Is_admin = 'FALSE' AND Username LIKE ?", [Username])
            member = c.fetchall()
            conn.commit()
            # If there are no users with that username, the result will be an empty list.
            # Therefore, if there are no members and the list is empty, it will print the below statement.
            # Otherwise it will display the details of the members
            if member == []:
                print("There is no member with this username")
            else:
                print("Below are the details of the user")
                for row in member:
                    print(row)
        except KeyError as e:
            print(e)

    # login function gets the username and password from the user, matches the values with the database and if they are an admin, logs in to the system.
    def login(self):
        Username = input("Please enter your username: ")
        Password = input("Please enter your password: ")

        try:
            # Here only the members who are included as admin are returned
            c.execute("SELECT Username, Password From Members WHERE Is_admin = 'TRUE'")
            login_details = c.fetchall()
            for details in login_details:
                # if the username matches with the username from the database, it prints the below statement.
                # Otherwise, it will give an error.
                if Username == details[0] and Password == details[1]:
                    print("Logged in successfully!")
                    return True
                else:
                    print("Loading.... Please check if the details you entered are correct")
                    return False
        except KeyError as e:
            print(e)

    # count_book method counts the number of book a particular member has in his account and returns the number.
    @classmethod
    def count_book_(cls, Username):
        try:
            c.execute("SELECT COUNT(*) FROM Books WHERE Loan_user = ?", [Username])
            book_count = (c.fetchone())[0]
            return book_count
        except KeyError as e:
            print(e)

    # check_membership methods gets the membership type for that particular user and returns its value
    @classmethod
    def check_membership(cls, Username):
        try:
            # Username = ('%' + Username + '%')
            c.execute("SELECT Membership_type FROM Members WHERE Username = ?", [Username])
            membership_type = (c.fetchone()[0])
            return membership_type
        except KeyError as e:
            print(e)

    # user_books method prints all the books a particular member has
    @classmethod
    def user_books(cls):
        Username = input("Please enter the username: ")
        try:
            c.execute("SELECT * FROM Books WHERE Loan_user = ?", [Username])
            books_user = c.fetchall()
            # Prints the rows in a separate line.
            for book in books_user:
                print("Books borrowed by this user: ", book)
        except KeyError as e:
            print(e)

    # issue_date methods returns the date the book was issued to a member.
    # This is saved to a variable in another function in the loan class
    @classmethod
    def issue_date(cls, ISBN):
        try:
            c.execute("SELECT Loan_date FROM Books WHERE ISBN = ?", [ISBN])
            date_issued = (c.fetchone()[0])
            date_issued = datetime.strptime(date_issued, "%d-%m-%Y").date()
            return date_issued
        except KeyError as e:
            print(e)

    # update_status method updates the status of the book to Available, removes the loan_user and the loan_date from the Books table for the book that is returned.
    # Only updates the status for a particular ISBN.
    @classmethod
    def update_status(cls, ISBN):
        try:
            c.execute("UPDATE Books SET Loan_status = 'Available',  Loan_user = '', Loan_date = '' WHERE ISBN = ?", [ISBN])
            print("Records are updated successfully!")
            conn.commit()
        except KeyError as e:
            print(e)

    # update_issue method updates the status, loan-date and member's username for the book that is issued to a particular member
    @classmethod
    def update_issue(cls, value):
        try:
            c.execute(
                '''UPDATE Books SET Loan_status = 'Loaned', Loan_date = (?), Loan_user = (?) WHERE ISBN == (?)''',
                (value[1], value[2], value[0]))
            conn.commit()
            print(f'Updated book details in the table')
        except KeyError as e:
            print(e)

    # logout method logs out from the application
    def logout(self):
        loop = False
        print("Logout successful!")

