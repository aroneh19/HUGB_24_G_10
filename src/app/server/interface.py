from logic import *

class SystemInterface:
  """A class representing our interface to the outside."""
  
  def __init__(self):
    self.user_logic = UserLogic()
    self.filter_logic = FilterLogic()
    self.message_logic = MessageLogic()

  def get_user(self):
    return self.user_logic.get_user()