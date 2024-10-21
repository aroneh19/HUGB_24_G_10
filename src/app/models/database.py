import json

class Database:
    def __init__(self):
        self.users_file = "app/data/users.json"
        self.messages_file = "app/data/messages.json"
        self.user_storage = self.load_users()

    def load_users(self):
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                users = json.load(file)
                print(f"Loaded users: {users}")  # Print loaded users to verify it's working
                return users
        except FileNotFoundError:
            print(f"Error: {self.users_file} not found.")
            return {}
        except Exception as e:
            print(f"Error loading users.json: {e}")  # Print any other errors
            return {}



    
    def save_users(self):
        """Save users to JSON file."""
        with open(self.users_file, 'w') as file:
            json.dump(self.user_storage, file, indent=4)
