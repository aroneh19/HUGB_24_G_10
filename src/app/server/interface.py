from app.models.database import Database
from app.logic.user_logic import UserLogic
from app.logic.filter_logic import FilterLogic
from app.logic.message_logic import MessageLogic
from app.logic.location_logic import LocationLogic
from app.views.mainmenu_view import MainMenuView
from app.views.login_view import LoginView
from app.logic.login_logic import LoginLogic

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
        self.location_logic = LocationLogic()

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