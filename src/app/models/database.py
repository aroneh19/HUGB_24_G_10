import json

class Database:
    def __init__(self, data_file="app/data/users.json"):
        self.data_file = data_file

    def load_users(self):
        """Load user data from the JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                users = json.load(file)
            return users
        except FileNotFoundError:
            print(f"Error: {self.data_file} not found.")
            return []
    
    def save_users(self):
        """Save users to JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.user_storage, file, indent=4)
