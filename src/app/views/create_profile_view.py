from app.logic.user_logic import UserLogic
from app.logic.location_logic import LocationLogic
from app.utils.utils import clearTerminal

class CreateProfileView:
    def __init__(self):
        self.user_logic = UserLogic()
        self.location_logic = LocationLogic()

        self.profile = {
            "username": None,
            "password": None,
            "name": None,
            "age": None,
            "bio": None,
            "interests": [],
            "location": None
        }

    def create_profile_menu(self):
        while True:
            print("=== Create a New Profile ===")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            fullname = input("Enter your name: ")
            age = input("Enter your age: ")
            bio = input("Write a short bio: ")
            interests = self.get_interests()
            location = self.get_location()

            coordinates = self.location_logic.get_location_coordinates(location)

            if "error" in coordinates:
                print(f"Error getting coordinates: {coordinates['error']}")
                continue

            success, message = self.user_logic.create_user(username, password, fullname, age, bio, interests, location, coordinates)
            if success:
                print(f"Profile for {username} created successfully!")
                break
            else:
                print(f"Failed to create profile: {message}")

    
    def get_interests(self):
        print("Please select your interests from the list below:")
        interests_list = [
            "Sports", "Books", "Music", "Movies", "Video Games", "Art", 
            "Cooking", "Fitness", "Travel", "Photography", "Fashion", 
            "Technology", "Science", "Gardening", "Hiking", "Yoga", 
            "Dancing", "Writing", "Meditation", "Gaming"
        ]
        selected_interests = []

        while True:
            clearTerminal()
            half_length = len(interests_list) // 2 + len(interests_list) % 2
            for i in range(half_length):
                left_item = f"{i+1}. {interests_list[i]}"
                right_item = f"{i+1+half_length}. {interests_list[i+half_length]}" if i+half_length < len(interests_list) else ""
                print(f"{left_item:<20} {right_item}")

            choice = input("\nEnter the number of your interest or 'd' to finish: ")
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
            clearTerminal()
            for i, location in enumerate(locations_list, 1):
                print(f"{i}. {location}")

            choice = input("\nEnter the number of your location: ")
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
    create_profile_view = CreateProfileView()
    create_profile_view.create_profile_menu()