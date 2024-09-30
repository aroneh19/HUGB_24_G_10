from app.models.database import Database
from app.logic.user_logic import UserLogic
from app.logic.filter_logic import FilterLogic
from app.logic.message_logic import MessageLogic
from app.views.mainmenu_view import MainMenuView

class SystemInterface:
    def __init__(self):
        self.db = Database()
        self.user_logic = UserLogic()
        self.filter_logic = FilterLogic()
        self.message_logic = MessageLogic()

    def main_menu(self):
        """Display the main menu."""
        main_menu = MainMenuView()
        main_menu.main_menu()

    def add_user(self, username, password, name, bio, interests, location):
        """Add a new user via UserLogic and save to the database."""
        success, msg = self.user_logic.create_user(username, password, name, bio, interests, location)
        
        if success:
            return {"message": msg}, 201
        else:
            return {"error": msg}, 400
