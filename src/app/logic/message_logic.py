from datetime import datetime
import json
from app.models.database import Database

class MessageLogic:
    def __init__(self):
        self.db = Database()

    def send_message(self, sender, receiver, message_text):
        """Send a message from sender to receiver and save it."""
        new_message = {
            "sender": sender,
            "receiver": receiver,
            "message": message_text,
            "time": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }

        # Load existing messages, append new message, and save
        messages = self.db.load_messages()
        messages["messages"].append(new_message)
        self.db.save_messages(messages)
        return {"status": "Message sent successfully"}

    def get_messages(self, user):
        """Retrieve all messages for a specific user."""
        messages = self.db.load_messages()["messages"]
        user_messages = [msg for msg in messages if msg["sender"] == user or msg["receiver"] == user]
        return user_messages
