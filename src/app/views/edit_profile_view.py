from app.logic.user_logic import UserLogic

class EditProfileView:
    def __init__(self, username):
        self.user_logic = UserLogic()
        self.username = username
        

    def display_edit_profile(self):
        print("Edit your profile:")
        
        while True:
            print("\nWhat would you like to edit?")
            print("1. Username")
            print("2. Password")
            print("3. Name")
            print("4. Age")
            print("5. Bio")
            print("6. Interests")
            print("7. Location")
            print("8. Exit Editing")
            choice = input("Enter Your Choice: ")
            
            if choice == "1":
                self.edit_username()
            elif choice == "2":
                self.edit_password()
            elif choice == "3":
                self.edit_name()
            elif choice == "4":
                self.edit_age()
            elif choice == "5":
                self.edit_bio()
            elif choice == "6":
                self.edit_interests()
            elif choice == "7":
                self.edit_location()
            elif choice == "8":
                break
            else:
                print("Invalid choice, try again.")

    def edit_username(self):
        new_username = input("Enter your new username: ")
        if self.user_logic.check_username(new_username):
            self.user_logic.edit_username(new_username)
            print("Username updated successfully!")
        else:
            print("Username already taken or invalid.")

    def edit_password(self):
        new_password = input("Enter your new password: ")
        self.user_logic.edit_password(new_password)
        print("Password updated successfully!")

    def edit_name(self):
        new_name = input("Enter your new name: ")
        self.user_logic.edit_name(new_name)
        print("Name updated successfully!")

    def edit_age(self):
        new_age = input("Enter your new age: ")
        if self.user_logic.check_age(new_age):
            self.user_logic.edit_age(new_age)
            print("Age updated successfully!")
        else:
            print("Invalid age.")

    def edit_bio(self):
        new_bio = input("Enter your new bio: ")
        self.user_logic.edit_bio(new_bio)
        print("Bio updated successfully!")

    def edit_interests(self):
        new_interests = self.get_interests()
        self.user_logic.edit_interests(new_interests)
        print("Interests updated successfully!")

    def edit_location(self):
        new_location = input("Enter your new location: ")
        self.user_logic.edit_location(new_location)
        print("Location updated successfully!")
    