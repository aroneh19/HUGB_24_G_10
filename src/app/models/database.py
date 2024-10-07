import json

class Database:
    def __init__(self):
        self.users_file = "app/data/users.json"
        self.messages_file = "app/data/messages.json"

    def load_users(self):
        """Load user data from the JSON file."""
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                if file.readable():
                    file.seek(0) 
                    content = file.read().strip()
                    if not content:
                        return []
                    else:
                        users = json.loads(content)
                        if isinstance(users, list):
                            return users
                        else:
                            return [] 
        except FileNotFoundError:
            print(f"Error: {self.users_file} not found.")
            return []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []


    
    def save_users(self, user_storage):
        """Save users to JSON file."""
        with open(self.users_file, 'w', encoding='utf-8') as file:
            json.dump(user_storage, file, ensure_ascii=False, indent=4)
