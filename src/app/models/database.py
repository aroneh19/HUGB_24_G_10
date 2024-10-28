import json

class Database:
    def __init__(self):
        self.users_file = "app/data/users.json"
        self.messages_file = "app/data/messages.json"
        self.user_storage = self.load_users()

    def load_users(self):
        """
        Load users from a JSON file.

        Returns:
        list: A list of users. If the file is not found or the content is not valid, an empty list is returned.
        """
        try:
            with open(self.users_file, 'r', encoding='utf-8') as file:
                users = json.load(file)
                return users
        except FileNotFoundError:
            print(f"Error: {self.users_file} not found.")
            return {}
        except Exception as e:
            print(f"Error loading users.json: {e}")  # Print any other errors
            return {}



    
    def save_users(self, user_storage):
        """
        Save users to a JSON file.

        Parameters:
        user_storage (list): The list of users to save.
        """
        with open(self.users_file, 'w', encoding='utf-8') as file:
            json.dump(user_storage, file, ensure_ascii=False, indent=4)
