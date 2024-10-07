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
                if isinstance(users, dict):
                    return users
                else:
                    return {}
        except FileNotFoundError:
            print(f"Error: {self.users_file} not found.")
            return {}

    
    def save_users(self, user_storage):
        """Save users to JSON file."""
        with open(self.users_file, 'w', encoding='utf-8') as file:
            json.dump(user_storage, file, ensure_ascii=False, indent=4)
