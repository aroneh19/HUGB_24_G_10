from app.logic.user_logic import UserLogic

class LoginView:
    """
    View responsible for handling user login.

    Attributes:
    user_logic (UserLogic): Handles user-related operations.
    """

    def __init__(self):
        """
        Initializes LoginView with an instance of UserLogic.
        """
        self.user_logic = UserLogic()

    def login_menu(self):
        """
        Displays the login menu and prompts the user for login credentials.
        Verifies the user and allows for retry if login fails.
        """
        from app.views.mainmenu_view import MainMenuView
        while True:
            print("=== Login ===")
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            success, message = self.user_logic.verify_user(username, password)
            if success:
                print(f"Welcome, {username}! You are now logged in.")
                return True  # Login successful
            else:
                print(f"Login failed: {message}")
                retry = input("Do you want to try again? (y/n): ")
                if retry.lower() != 'y':
                    return False  # User opts not to retry
