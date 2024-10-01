import json

class Database:
    def __init__(self):
        self.users_file = "app/data/users.json"
        self.messages_file = "app/data/messages.json"

    def load_users(self):
        """Load user data from the JSON file."""
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                users = json.load(file)
            return users
        except FileNotFoundError:
            print(f"Error: {self.users_file} not found.")
            return []
    
    def save_users(self):
        """Save users to JSON file."""
        with open(self.users_file, 'w') as file:
            json.dump(self.user_storage, file, indent=4)
