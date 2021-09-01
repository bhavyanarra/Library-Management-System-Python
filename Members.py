from Functions import Update_data

# A separate class is created for the members which adds and updates member details.
# The parent class for this class is Update_data which inherits all the methods used for database updates

class Members(Update_data):

    def __init__(self):
        super().__init__()

    # This method is used to add members to the Members table in library database.
    def add_members(self):
        self.Username = input("Please enter an email ID for username: ")
        self.Password = input("Please enter a password for this user: ")
        self.Name = input("Please enter the full name of the member: ")
        self.Address = input("Please enter the member's address: ")
        self.Contact_number = input("Please enter the contact number: ")
        self.Membership_type = input("Please enter the membership type (Basic / Premium): ")
        self.Is_admin = str(input("Please enter if this member is an admin (TRUE/FALSE): "))

        # All the values entered above are passed to a list
        new_member = [[self.Username, self.Password, self.Name, self.Address, self.Contact_number, self.Membership_type, self.Is_admin]]
        # add_member method is inherited from the parent class which updates the above values in the members table in database.
        super().add_member('values(?, ?, ?, ?, ?, ?, ?)', new_member[0])

    # This method updates member details in the database
    def update_members(self):
        self.Username = input("Please enter an email ID for username: ")
        self.Password = input("Please enter a password for this user: ")
        self.Name = input("Please enter the full name of the member: ")
        self.Address = input("Please enter the member's address: ")
        self.Contact_number = input("Please enter the contact number: ")
        self.Membership_type = input("Please enter the membership type (Basic / Premium): ")
        self.Is_admin = str(input("Please enter if this member is an admin (TRUE/FALSE): "))

        # The values entered by the user is stored as a list
        member_value = [self.Username, self.Password, self.Name, self.Address, self.Contact_number, self.Membership_type, self.Is_admin]
        # Update_member is inherited from the parent class and is used for updating the database
        super().update_member(member_value)


# Test codes. Provided as reference only. These codes have been used in the main application.
bc = Members()

bc.create_connection("library.db")
#bc.add_members()#"bcd@gmail.com", "asddfg", "Julien", "BCD, Belfast", 7894561230, "Premium", "TRUE")
#bc.update_members() #"bcd@gmail.com", "cat123", "Julien", "BCD, Belfast", 7894561230, "Premium", "FALSE")
#bc.delete_member()
#bc.search_member()
#bc.login()
