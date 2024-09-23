from logic.profile_logic import ProfileLogic
from logic.filter_logic import FilterLogic  # Assuming you have these classes
from logic.message_logic import MessageLogic  # Assuming these exist

class SystemInterface:
    """A class representing our interface to the outside."""
  
    def __init__(self):
        self.user_logic = ProfileLogic()
        self.filter_logic = FilterLogic()
        self.message_logic = MessageLogic()

    def get_users(self):
        return self.user_logic.get_all_users()

    def add_user(self, user_data):
        return self.user_logic.create_user(user_data)
