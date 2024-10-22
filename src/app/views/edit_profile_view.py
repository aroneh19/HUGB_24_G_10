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
        new_location = self.get_location()
        coordinates = self.location_logic.get_location_coordinates(new_location)

        if "error" in coordinates:
            print(f"Error updating location: {coordinates['error']}")
        else:
            success, message = self.user_logic.edit_location(new_location, coordinates)
            print(message)

    def get_interests(self):
        interests_list = [
            "Sports", "Books", "Music", "Movies", "Video Games", "Art", 
            "Cooking", "Fitness", "Travel", "Photography", "Fashion", 
            "Technology", "Science", "Gardening", "Hiking", "Yoga", 
            "Dancing", "Writing", "Meditation", "Gaming"
        ]
        selected_interests = []

        while True:
            for i, interest in enumerate(interests_list, 1):
                print(f"{i}. {interest}")
            print("Type 'b' to finish selecting interests.")

            choice = input("Enter the number of your interest: ")
            if choice == "d":
                if selected_interests:
                    break
                else:
                    print("You must select at least one interest.")
            else:
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(interests_list):
                        selected_interests.append(interests_list[index])
                        print(f"Selected interests: {selected_interests}")
                    else:
                        print("Invalid choice, please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        return selected_interests
    
    def get_location(self):
        locations_list = [
            "Reykjavík", "Kópavogur", "Akureyri", "Mosfellsbær", "Hafnarfjörður",
            "Selfoss", "Akranes", "Vestmannaeyjar"
        ]

        while True:
            for i, location in enumerate(locations_list, 1):
                print(f"{i}. {location}")

            choice = input("Enter the number of your location: ")
            try:
                index = int(choice) - 1
                if 0 <= index < len(locations_list):
                    selected_location = locations_list[index]
                    print(f"Selected location: {selected_location}")
                    return selected_location
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    edit_profile_view = EditProfileView("aron")  # Ensure 'aron' exists in the JSON file
    edit_profile_view.display_edit_profile()
