from app.utils.utils import clearTerminal

class LoginView:
    """
    View responsible for handling user login.

    Attributes:
    user_logic (UserLogic): Handles user-related operations.
    """

    def __init__(self, user_logic):
        """
        Initializes LoginView with an instance of UserLogic.
        """
        self.user_logic = user_logic

    def login_menu(self):
        """
        Displays the login menu and prompts the user for login credentials.
        Verifies the user and allows for retry if login fails.
        """
        while True:
            clearTerminal()
            print("=== Login ===")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            success, result = self.user_logic.verify_user(username, password)
            if success:
                return result  
            else:
                print(f"Login failed: {result}")
                retry = input("Do you want to try again? (y/n): ")
                if retry.lower() != 'y':
                    return False  # User opts not to retry
