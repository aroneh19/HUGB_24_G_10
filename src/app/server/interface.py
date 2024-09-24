from app.logic.user_logic import UserLogic
from app.logic.filter_logic import FilterLogic
from app.logic.message_logic import MessageLogic

class SystemInterface:
    """A class representing our interface to the outside."""
  
    def __init__(self):
        self.user_logic = UserLogic()
        self.filter_logic = FilterLogic()
        self.message_logic = MessageLogic()

    def get_users(self):
        return self.user_logic.get_all_users()

    def add_user(self, user_data):
        return self.user_logic.create_user(user_data)
    
    def an_operation_without_params(self):
        return {"msg": "Operation successful"}
