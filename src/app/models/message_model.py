import json
from datetime import datetime

class Message:
    def __init__(self, sender, receiver, message):
        """
        Initializes the Message with the sender, receiver, message, and the current time.

        Parameters:
        sender (str): The sender of the message.
        receiver (str): The receiver of the message.
        message (str): The message.
        """
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.time = datetime.datetime.now()
    
    def to_json(self):
        """
        Convert the message to a json string.

        Returns:
        str: A json string representing the message.
        """
        return json.dumps(self.__dict__)

def load_message(user, path="data/messages.json"):
    import json
from datetime import datetime

class Message:
    """A class to handle operations related to messages."""

    def __init__(self, sender, receiver, message):
        """
        Initializes the Message with the sender, receiver, message, and the current time.

        Parameters:
        sender (str): The sender of the message.
        receiver (str): The receiver of the message.
        message (str): The message.
        """
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.time = datetime.now()
    
    def to_json(self):
        """
        Convert the message to a json string.

        Returns:
        str: A json string representing the message.
        """
        return json.dumps(self.__dict__)

def load_message(user, path="data/messages.json"):
    """
    Load all messages from the json file.

    Parameters:
    user (str): The user whose messages to load.
    path (str): The path to the json file.

    Returns:
    list: A list of Message objects.
    """
    with open(path, 'r') as file:
        messages = json.load(file)
    return [Message(**message) for message in messages if message["sender"] == user or message["receiver"] == user]

def save_message(messages, path="data/messages.json"):
    pass