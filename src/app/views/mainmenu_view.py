import sys
from app.views.filter_view import FilterView
from app.views.swiping_view import SwipingView
from app.views.edit_profile_view import EditProfileView
from app.utils.utils import clearTerminal

class MainMenuView:
    """
    View responsible for displaying and handling the main menu options.

    Attributes:
    username (str): Stores the username of the logged-in user.
    filter (FilterView): Handles filtering functionality.
    swiping (SwipingView): Handles swiping functionality.
    """

    def __init__(self, user_logic) -> None:
        """
        Initializes MainMenuView with the username and instances of FilterView and SwipingView.

        Attributes:
        username (str): Username of the logged-in user.
        filter (FilterView): Manages filtering logic.
        swiping (SwipingView): Manages swiping logic.
        """
        self.user_logic = user_logic
        self.filter = FilterView()
        self.swiping = SwipingView()
    
    def display_menu(self):
        """
        Displays the main menu options.
        """
        clearTerminal()
        print("1. Start Swiping")
        print("2. Filter")
        print("3. Messages")
        print("4. Profile")
        print("5. Edit Profile")

    def main_menu(self):
        """
        Handles user input for navigating the main menu.
        """
        while True:
            self.display_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.swiping.start_swiping(self.filter.filter)
            elif choice == "2":
                self.filter.filter_menu()
            elif choice == "3":
                print("Messages")
            elif choice == "4":
                print("Profile")
            elif choice == "5":
                edit_view = EditProfileView(self.user_logic.current_user)
                edit_view.display_edit_profile()
            else:
                print("Invalid choice, try again.")
