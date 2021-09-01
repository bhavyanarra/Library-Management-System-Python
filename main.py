from Functions import Update_data
from Books import Books
from Loan import Loan
from Members import Members

# Creating variables and calling the functions.
lib = Update_data()
mem = Members()
bk = Books()
ln = Loan()

# Creating a function to display the main menu for the library and asks the user for the number input and returns its value
def main_menu():
    print("-------------------------Welcome to the Library------------------------")
    print("Main Menu")
    print("1. Books: View, Add and update book details in the library database")
    print("2. Members: View, Add or update member details in the library database")
    print("3. Loan: Issue books, return books, search books on loan, check members who borrowed books")
    print("4. Logout")
    print("------------------------------------------------------------------------")
    choice = int(input("Please enter a number from 1 to 4 from the above menu: "))
    return choice

# Below function helps in displaying the Books menu for the library and asks the user for the number input and returns its value
def book_menu():
    print("-----Books Menu-----")
    print("1. Add Books")
    print("2. Update book details")
    print("3. Search books")
    print("4. Delete books")
    print("5. Logout")
    print("--------------------")
    print("Enter any other number for returning to the main menu")
    sel = int(input("Please enter a number from the options above: "))
    return sel

# This function displays the member menu for the library and asks the user for the number input and returns its value
def member_menu():
    print("-----Members Menu-----")
    print("1. Add Member")
    print("2. Update member details")
    print("3. Search member")
    print("4. Delete member")
    print("5. Logout")
    print("----------------------")
    print("Enter any other number for returning to the main menu")
    ch1 = int(input("Please enter a number from the options above: "))
    return ch1

# This function displays the Loan menu for the library and asks the user for the number input and returns its value
def Loan_menu():
    print("-----Loan Menu-----")
    print("1. Search books available in the library")
    print("2. Issue book to the member")
    print("3. Return book")
    print("4. Search books under a member")
    print("5. Logout")
    print("-------------------")
    print("Enter any other number for returning to the main menu")
    ch2 = int(input("Please enter a number from the options above: "))
    return ch2

# Below code runs the application: All the above functions and classes created are used in this code chunk.
# For logging in, please use Username: abc@gmail.com and Password: abc123. Any username or password other than that will give an error.

if __name__ == "__main__":
    if (lib.login() == True):
        loop = True
        # While loop is added so that it returns to the main menu after the previous code is executed
        while loop:
            choice = main_menu()
            # Choice 1 presents the Books menu and the code is given for each of the actions in the menu.
            if choice == 1:
                sel = book_menu()
                if sel == 1:
                    bk.add_books()
                elif sel == 2:
                    bk.update_books()
                elif sel == 3:
                    bk.search_book()
                elif sel == 4:
                    bk.delete_book()
                elif sel == 5:
                    loop = False
                    lib.logout()
                else:
                    print("Press any other number for the main menu")
            # Choice 2 represents the Members menu
            elif choice == 2:
                ch1 = member_menu()
                if ch1 == 1:
                    mem.add_members()
                elif ch1 == 2:
                    mem.update_members()
                elif ch1 == 3:
                    mem.search_member()
                elif ch1 == 4:
                    mem.delete_member()
                elif ch1 == 5:
                    loop = False
                    lib.logout()
                else:
                    print("Press any other number for the main menu")
            # Choice 3 presents the Loan menu
            elif choice == 3:
                ch2 = Loan_menu()
                if ch2 == 1:
                    ln.view_books()
                elif ch2 == 2:
                    ln.issue_books()
                elif ch2 == 3:
                    ln.return_book()
                elif ch2 == 4:
                    ln.user_books()
                elif ch2 == 5:
                    lib.logout()
                else:
                    print("Press any other number to return to the main menu")
            else:
                loop = False
                lib.logout()
            # At each of the above functions, there is a logout code which logs out the user from the system.
    # Below code is printed when the username or password does not match with the records in the database.
    else:
        print("Username or Password is incorrect!")