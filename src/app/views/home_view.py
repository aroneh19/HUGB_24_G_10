from app.views.login_view import LoginView
from app.views.create_profile_view import CreateProfileView
from app.views.mainmenu_view import MainMenuView
from app.logic.user_logic import UserLogic

class HomeView:
    """
    Home View responsible for providing the user with options to create a user or log in.
    """

    def __init__(self):
        self.user_logic = UserLogic()
        self.login_view = LoginView(self.user_logic)
        self.create_profile_view = CreateProfileView(self.user_logic)
        self.main_menu_view = None

    def display_menu(self):
        """
        Display the home menu and handle user choices.
        """
        while True:
            print("=== Home Screen ===")
            print("1. Create User")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                user = self.create_profile_view.create_profile_menu()
            elif choice == '2':
                user = self.login_view.login_menu()
            elif choice == '3':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
                continue

            if user:
                self.main_menu_view = MainMenuView(self.user_logic, user)
                self.main_menu_view.main_menu() 

if __name__ == "__main__":
    home_view = HomeView()
    home_view.display_menu()
