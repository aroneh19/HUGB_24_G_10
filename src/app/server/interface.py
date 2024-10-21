from app.models.database import Database
from app.logic.user_logic import UserLogic
from app.logic.filter_logic import FilterLogic
from app.logic.message_logic import MessageLogic
from app.logic.location_logic import LocationLogic
from app.views.mainmenu_view import MainMenuView

class SystemInterface:
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
        """Add a new user via UserLogic and save to the database."""
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
        """Get all users from the database."""
        users = self.db.load_users()
        return users