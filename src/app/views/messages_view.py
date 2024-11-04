from app.logic.message_logic import MessageLogic

class MessageView:
    def __init__(self, username):
        self.username = username
        self.message_logic = MessageLogic()

    def display_message_menu(self):
        while True:
            print("\n=== Messages Menu ===")
            print("1. Send a Message")
            print("2. View Messages")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.send_message()
            elif choice == "2":
                self.view_messages()
            elif choice == "3":
                break
            else:
                print("Invalid choice, try again.")

    def send_message(self):
        receiver = input("Enter the receiver's username: ")
        message_text = input("Enter your message: ")
        response = self.message_logic.send_message(self.username, receiver, message_text)
        print(response.get("status"))

    def view_messages(self):
        messages = self.message_logic.get_messages(self.username)
        if messages:
            print("\n--- Your Messages ---")
            for msg in messages:
                print(f"[{msg['time']}] {msg['sender']} to {msg['receiver']}: {msg['message']}")
        else:
            print("No messages found.")

if __name__ == "__main__":
    view = MessageView("aron")
    view.display_message_menu()