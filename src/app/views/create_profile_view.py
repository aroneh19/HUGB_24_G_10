from app.logic.user_logic import UserLogic 
from app.logic.location_logic import LocationLogic
from app.utils.utils import clearTerminal

class CreateProfileView:
    """
    View responsible for creating a new user profile.

    Attributes:
    user_logic (UserLogic): Handles user-related operations.
    location_logic (LocationLogic): Handles location-related operations.
    profile (dict): Stores profile information.
    """
    
    def __init__(self, user_logic):
        """
        Initializes CreateProfileView with UserLogic and LocationLogic instances.

        Attributes:
        user_logic (UserLogic): Manages user-related logic.
        location_logic (LocationLogic): Manages location-related operations.
        profile (dict): Stores profile information.
        """
        self.user_logic = user_logic
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
        """Displays the profile creation menu and handles user input for the profile."""
        while True:
            clearTerminal()
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

            success, message = self.user_logic.create_user(
                username, password, fullname, age, bio, interests, location, coordinates
            )
            if success:
                print(f"Profile for {username} created successfully!")
                return True
            else:
                print(f"Failed to create profile: {message}")

    def get_interests(self):
        """
        Prompts the user to select interests from a predefined list.

        Returns:
        list: A list of selected interests.
        """
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
                    return selected_location
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
