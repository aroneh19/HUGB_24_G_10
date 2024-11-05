# matches_view.py
from app.logic.matches_logic import MatchesLogic
from app.models.database import Database
from app.utils.utils import clearTerminal
from datetime import datetime


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
        Displays the profile of a selected match and allows viewing the conversation history and sending a message.

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
            
            # Display conversation history
            print("\n--- Conversation History ---")
            self.display_conversation(match_username)
            
            # Prompt to send a message after viewing conversation
            self.send_message_prompt(match_username)
        else:
            print("Error: Could not find the selected user's profile.")

    
    def send_message_prompt(self, match_username):
        """
        Prompts the user to send a message to the selected match or unmatch them.

        Args:
            match_username (str): The username of the selected match.
        """
        while True:
            message = input(f"Enter a message to send to {match_username} (or type 'back' to return, 'unmatch' to remove match): ")
            
            # Option to go back
            if message.lower() == 'back':
                break
            
            # Option to unmatch
            elif message.lower() == 'unmatch':
                confirm_unmatch = input(f"Are you sure you want to unmatch with {match_username}? (y/n): ")
                if confirm_unmatch.lower() == 'y':
                    self.unmatch_user(match_username)
                    print(f"You have unmatched with {match_username}.")
                    break  # Exit the prompt after unmatching
                else:
                    print("Unmatch canceled.")
            
            # Sending a non-empty message
            elif message.strip():
                self.send_message(match_username, message)
                print(f"Message sent to {match_username}: {message}")
            
            # Handle empty message input
            else:
                print("Message cannot be empty.")


    def send_message(self, recipient, message):
        """
        Simulates sending a message by saving it in the messages file.

        Args:
            recipient (str): The username of the recipient.
            message (str): The content of the message.
        """
        # Load or initialize the messages data as a dictionary with a "messages" list
        messages_data = self.database.load_data(self.database.messages_file)
        
        # Ensure "messages" is a list within the dictionary
        if "messages" not in messages_data or not isinstance(messages_data["messages"], list):
            messages_data["messages"] = []

        # Append the new message to the "messages" list
        messages_data["messages"].append({
            "sender": self.current_user['username'],
            "receiver": recipient,
            "message": message,
            "time": str(datetime.now())  # This line should work now
        })

        # Save the updated messages dictionary back to the file
        self.database.save_data(self.database.messages_file, messages_data)

    def display_conversation(self, match_username):
        """
        Displays the conversation history between the current user and a match.

        Args:
            match_username (str): The username of the match to display messages with.
        """
        messages_data = self.database.load_data(self.database.messages_file)
        conversation = [
            msg for msg in messages_data.get("messages", [])
            if (msg["sender"] == self.current_user['username'] and msg["receiver"] == match_username) or
            (msg["sender"] == match_username and msg["receiver"] == self.current_user['username'])
        ]

        if conversation:
            for msg in conversation:
                sender = "You" if msg["sender"] == self.current_user['username'] else msg["sender"]
                print(f"{sender}: {msg['message']} ({msg['time']})")
        else:
            print("No messages with this user yet.")

    def unmatch_user(self, match_username):
        """
        Removes the match between the current user and the specified match.

        Args:
            match_username (str): The username of the match to unmatch.
        """
        self.matches_logic.unmatch(self.current_user['username'], match_username)
        print(f"You have unmatched with {match_username}.")

