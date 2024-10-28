from app.logic.user_logic import UserLogic

class EditProfileView:
    """
    View responsible for editing an existing user profile.

    Attributes:
    user_logic (UserLogic): Handles user-related operations.
    username (str): Stores the username of the profile to be edited.
    """

    def __init__(self, username):
        """
        Initializes EditProfileView with the username of the profile to edit.

        Attributes:
        user_logic (UserLogic): Manages user-related logic.
        username (str): Username of the profile to be edited.
        """
        self.user_logic = UserLogic()
        self.user_logic.set_current_user(username)  # Set the current user here
        self.username = username

    def display_edit_profile(self):
        """
        Displays the edit profile menu and handles user input for editing profile fields.
        """
        print("Edit your profile:")
        
        while True:
            print("\nWhat would you like to edit?")
            print("1. Bio")
            print("2. Interests")
            print("3. Location")
            print("4. Exit Editing")
            choice = input("Enter Your Choice: ")
            
            if choice == "1":
                self.edit_bio()
            elif choice == "2":
                self.edit_interests()
            elif choice == "3":
                self.edit_location()
            elif choice == "4":
                break
            else:
                print("Invalid choice, try again.")

    def edit_username(self):
        """
        Edits the username of the profile.
        """
        new_username = input("Enter your new username: ")
        if self.user_logic.check_username(new_username):
            self.user_logic.edit_username(new_username)
            print("Username updated successfully!")
        else:
            print("Username already taken or invalid.")

    def edit_password(self):
        """
        Edits the password of the profile.
        """
        new_password = input("Enter your new password: ")
        self.user_logic.edit_password(new_password)
        print("Password updated successfully!")

    def edit_name(self):
        """
        Edits the name of the profile.
        """
        new_name = input("Enter your new name: ")
        self.user_logic.edit_name(new_name)
        print("Name updated successfully!")

    def edit_age(self):
        """
        Edits the age of the profile.
        """
        new_age = input("Enter your new age: ")
        if self.user_logic.check_age(new_age):
            self.user_logic.edit_age(new_age)
            print("Age updated successfully!")
        else:
            print("Invalid age.")

    def edit_bio(self):
        """
        Edits the bio of the profile.
        """
        new_bio = input("Enter your new bio: ")
        self.user_logic.edit_bio(new_bio)
        print("Bio updated successfully!")

    def edit_interests(self):
        """
        Edits the interests of the profile.
        """
        new_interests = self.get_interests()
        self.user_logic.edit_interests(new_interests)
        print("Interests updated successfully!")

    def edit_location(self):
        new_location = input("Enter your new location: ")
        self.user_logic.edit_location(new_location)
        print("Location updated successfully!")
    