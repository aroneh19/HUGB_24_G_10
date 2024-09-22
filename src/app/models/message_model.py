import json
from datetime import datetime

class Message:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.time = datetime.datetime.now()
    
    def to_json(self):
        """Convert the message to a json string."""
        return json.dumps(self.__dict__)

def load_message(user, path="data/messages.json"):
    """Load all messages from the json file."""
    with open(path, 'r') as file:
        messages = json.load(file)
    return [Message(**message) for message in messages if message["sender"] == user or message["receiver"] == user]

def save_message(messages, path="data/messages.json"):
    pass