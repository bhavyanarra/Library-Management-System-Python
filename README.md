# Description
The main objective of this project is to design a system for library admin staff in order to manage their database. 
Three main classes were created which handles the updates that were to be made in the database relating to the three main areas,
 - Members, - Books and - Loan. Various functions with sqlite and object oriented programming were used in this project.

## History
	Initial version: 12 August 2021
	Draft version: 19 August 2021
	Final Version: 22 August 2021

## Installation:
Below packages are required to be installed for the application to run.
1. SQLite3
2. datetime
3. timedelta

# Author
## Name - Bhavya Narra

# Instructions:
There are 5 python files in the folder. The application is developed in main.py folder. Please run this file to get to the application.

For the login page, please use the below login details:
Username - abc@gmail.com
Password - abc123

Details of the python files are given below:

## a. main.py:
	- Includes a few functions to display the menu for the application, one for the main menu, one function for books menu, one for members menu and finally for the loan menu
	- Imports the classes and functions from all the other python files.
	- While loop is used to display the menu and if else statements are used to execute the code based on user's choice.

## b. Functions.py:
	- Includes a function to connect to the database
	- A parent class Update_data has been created to perform all SQL queries and execute it. Using conn.commit(), the updates made are saved to the database.
	- Contains functions to add, update, delete books and members. Also contains functions which can return few values like membership type or issue date which is used in the child class.
	- Has all SQL Wrapper functions in this class.

## c. Books.py:
	- A child class created for books which inherits few functions from the parent class, Update_data.
	- A book can be added, updated, searched based on title, or deleted from the database.
	- Two main functions created in this class are add_books and update_books. The other functions are inherited from the parent class.
	- Also includes test codes for demonstration. Remove the # before the code and execute the code.

## d. Members.py:
	- A child class created for members which inherits few functions from the parent class, Update_data.
	- Similar to Books class, Members class can add, update delete or search members based on their username.
	- The two main functions created in this class are add_members and update members. Other functions are inherited from parent class.
	- Also includes test codes for reference. Remove the # before the code and execute the code.

## e. Loan.py:
	- A child class created for issuing books on loan which inherits few functions from the parent class, Update_data.
	- In this class, a user can search for the books borrowed by a user, search for the books available in the library, issue books to a member and also, update the database for returned books and display the fine if applicable.
	- The main functions are view_books, issue_books and return book.
	- Also includes test codes for reference. Remove the # before the code and execute the code.