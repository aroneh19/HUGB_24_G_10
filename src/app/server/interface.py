from app.models.database import Database
from app.logic.user_logic import UserLogic
from app.logic.filter_logic import FilterLogic
from app.logic.message_logic import MessageLogic
from app.logic.location_logic import LocationLogic
# from app.views.mainmenu_view import MainMenuView
from app.views.login_view import LoginView
from app.logic.login_logic import LoginLogic
import json
import os

class SystemInterface:

    def start_app(self):
        print("===Welcome to Meet4Real====")

        if self.login_menu():
            self.main_menu()

        else: 
            print("Login Error.")   
        
    def __init__(self):
        self.db = Database()
        self.user_logic = UserLogic()
        self.filter_logic = FilterLogic()
        self.message_logic = MessageLogic()
        self.login_logic = LoginLogic()
        self.swipes_file = "app\data\swipes.json"
        self.matches_file = "app\data\matches.json"

    def login_menu(self):
        login_view = LoginView()
        success = login_view.login_menu()
        if not success:
            print("Invalid login credentials.")
        return success

    def main_menu(self):
        """Display the main menu."""
        main_menu = MainMenuView()
        main_menu.main_menu()

    def add_user(self, username, password, fullname, interests, location, age, bio):
        """
        Add a new user via UserLogic and save to the database.

        Parameters:
        username (str): The username of the user.
        password (str): The password of the user.
        fullname (str): The full name of the user.
        interests (list[str]): The interests of the user.
        location (str): The location of the user.
        age (int): The age of the user.
        bio (str): The bio of the user.

        Returns:
        dict: A dictionary containing a message or an error.
        int: A status code.
        """
        # Get coordinates from Geoapify
        coordinates = self.location_logic.get_location_coordinates(location)

        if "error" in coordinates:
            return {"error": coordinates["error"]}, 400
        
        success, msg = self.user_logic.create_user(username, password, fullname, interests, location, age, bio, coordinates)
        
        if success:
            return {"message": msg}, 201
        else:
            return {"error": msg}, 400

    def get_users(self):
        """
        Get all users from the database.

        Returns:
        list: A list of users.
        """
        users = self.db.load_users()
        return users

    def load_data(self, file_path):
            """Load data from a JSON file or return an empty dictionary if the file doesn't exist."""
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    return json.load(file)
            return {}

    def save_data(self, file_path, data):
        """Save data to a JSON file."""
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    def log_swipe_action(self, current_user, target_user, action):
        """
        Log a swipe action ("like" or "pass") and check for a mutual match if the action is a "like".
        
        Parameters:
        current_user (str): The username of the user swiping.
        target_user (str): The username of the user being swiped on.
        action (str): "like" or "pass" action.
        """
        # Load swipes data
        swipes = self.load_data(self.swipes_file)

        # Ensure current user has a dictionary entry
        if current_user not in swipes:
            swipes[current_user] = {"liked": [], "passed": []}

        # Log the action
        if action == "like":
            swipes[current_user]["liked"].append(target_user)
            # Check if target_user has already liked current_user
            if target_user in swipes and current_user in swipes[target_user]["liked"]:
                self.add_match(current_user, target_user)
        elif action == "pass":
            swipes[current_user]["passed"].append(target_user)

        # Save updated swipes data
        self.save_data(self.swipes_file, swipes)

    def add_match(self, user1, user2):
        """
        Record a mutual match between two users.
        
        Parameters:
        user1 (str): The username of the first user.
        user2 (str): The username of the second user.
        """
        # Load existing matches
        matches = self.load_data(self.matches_file)

        # Add the match entry if it doesn't already exist
        if {"user1": user1, "user2": user2} not in matches and {"user1": user2, "user2": user1} not in matches:
            matches.append({"user1": user1, "user2": user2})

        # Save the updated matches
        self.save_data(self.matches_file, matches)