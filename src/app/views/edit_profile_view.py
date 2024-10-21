from app.logic.user_logic import UserLogic

class EditProfileView:
    def __init__(self, username):
        self.user_logic = UserLogic()
        self.user_logic.set_current_user(username)  # Set the current user here
        self.username = username
        
        # Check if current_user is set correctly
        if self.user_logic.current_user is None:
            print("User not found. Please ensure the username is correct.")

    def display_edit_profile(self):
        if self.user_logic.current_user is None:
            print("No user is logged in.")
            return
        
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
        success, message = self.user_logic.edit_location(new_location)
        print(message)

    

if __name__ == "__main__":
    edit_profile_view = EditProfileView("aron")  # Ensure 'aron' exists in the JSON file
    edit_profile_view.display_edit_profile()
