# matches_view.py
from app.logic.matches_logic import MatchesLogic
from app.models.database import Database
from app.utils.utils import clearTerminal


class MatchesView:
    """
    View responsible for displaying the matches for the current user.
    """

    def __init__(self, current_user):
        """
        Initializes MatchesView with current user and matches logic.

        Args:
            current_user: The currently logged-in user object.
            database: An instance of the Database class for data access.
        """
        self.current_user = current_user
        self.database = Database()
        self.matches_logic = MatchesLogic(self.database)

    def display_matches(self):
        """
        Retrieves and displays the list of matches for the current user, allowing them to select a match to view.
        """
        matches = self.matches_logic.get_matches(self.current_user['username'])
        if not matches:
            print("No matches found.")
            return

        while True:
            clearTerminal()
            print("Your Matches:")
            for n, match in enumerate(matches, 1):
                print(f"{n}. {match}")

            choice = input("Select a match by number to view their profile or 'q' to quit: ")
            if choice.lower() == 'q':
                break
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                selected_match = matches[int(choice) - 1]
                self.view_match_profile(selected_match)
            else:
                print("Invalid choice, please try again.")

    def view_match_profile(self, match_username):
        """
        Displays the profile of a selected match and allows sending a message.

        Args:
            match_username (str): The username of the selected match.
        """
        users = self.database.load_data(self.database.users_file)
        match_profile = next((user for user in users if user["username"] == match_username), None)

        if match_profile:
            print("\n--- Profile ---")
            print(f"Full Name: {match_profile['fullname']}")
            print(f"Age: {match_profile['age']}")
            print(f"Location: {match_profile['location']['city']}")
            print(f"Interests: {', '.join(match_profile['interests'])}")
            print(f"Bio: {match_profile['bio']}")
            self.send_message_prompt(match_username)
        else:
            print("Error: Could not find the selected user's profile.")

    def send_message_prompt(self, match_username):
        """
        Prompts the user to send a message to the selected match.

        Args:
            match_username (str): The username of the selected match.
        """
        while True:
            message = input(f"Enter a message to send to {match_username} (or type 'back' to return): ")
            if message.lower() == 'back':
                break
            elif message.strip():
                self.send_message(match_username, message)
                print(f"Message sent to {match_username}: {message}")
            else:
                print("Message cannot be empty.")

    def send_message(self, recipient, message):
        """
        Simulates sending a message by saving it in the messages file.

        Args:
            recipient (str): The username of the recipient.
            message (str): The content of the message.
        """
        messages = self.database.load_data(self.database.messages_file)
        messages.append({
            "sender": self.current_user['username'],
            "recipient": recipient,
            "message": message
        })
        self.database.save_data(self.database.messages_file, messages)
