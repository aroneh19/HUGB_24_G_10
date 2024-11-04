import json
import os

class Database:
    def __init__(self):
        self.users_file = "app/data/users.json"
        self.messages_file = "app/data/messages.json"
        self.swipes_file = "app/data/swipes.json"
        self.matches_file = "app/data/matches.json"
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
            print(f"Error loading users.json: {e}") 
            return {}

    def save_users(self, user_storage):
        """
        Save users to a JSON file.

        Parameters:
        user_storage (list): The list of users to save.
        """
        with open(self.users_file, 'w', encoding='utf-8') as file:
            json.dump(user_storage, file, ensure_ascii=False, indent=4)

    def load_messages(self):
        """Load all messages from the JSON file."""
        try:
            with open(self.messages_file, 'r', encoding='utf-8') as file:
                if file.readable():
                    file.seek(0)
                    content = file.read().strip()
                    if not content:
                        return {"messages": []}
                    else:
                        return json.loads(content)
        except FileNotFoundError:
            print(f"Error: {self.messages_file} not found.")
            return {"messages": []}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {"messages": []}

    def save_messages(self, messages_data):
        """Save messages to JSON file."""
        with open(self.messages_file, 'w', encoding='utf-8') as file:
            json.dump(messages_data, file, ensure_ascii=False, indent=4)
    def load_data(self, file_path):
        """Helper function to load JSON data or return an empty list if the file is missing."""
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        return []

    def save_data(self, file_path, data):
        """Helper function to save data to a JSON file."""
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    # Methods for managing swipes
    def add_swipe(self, current_user, target_user, action):
        swipes = self.load_data(self.swipes_file)
        if current_user not in swipes:
            swipes[current_user] = {"liked": [], "passed": []}
        if action == "like" and target_user not in swipes[current_user]["liked"]:
            swipes[current_user]["liked"].append(target_user)
        elif action == "pass" and target_user not in swipes[current_user]["passed"]:
            swipes[current_user]["passed"].append(target_user)
        self.save_data(self.swipes_file, swipes)

    # Methods for managing matches
    def add_match(self, user1, user2):
        matches = self.load_data(self.matches_file)
        if {"user1": user1, "user2": user2} not in matches and {"user1": user2, "user2": user1} not in matches:
            matches.append({"user1": user1, "user2": user2})
        self.save_data(self.matches_file, matches)

    # def remove_match(self, user1, user2):
    #     matches = self.load_data(self.matches_file)
    #     matches = [match for match in matches if not (
    #         (match["user1"] == user1 and match["user2"] == user2) or
    #         (match["user1"] == user2 and match["user2"] == user1)
    #     )]
    #     self.save_data(self.matches_file, matches)
