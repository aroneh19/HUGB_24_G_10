import sys
from app.views.filter_view import FilterView
from app.views.swiping_view import SwipingView
from app.views.edit_profile_view import EditProfileView

class MainMenuView:
    """
    View responsible for displaying and handling the main menu options.

    Attributes:
    username (str): Stores the username of the logged-in user.
    filter (FilterView): Handles filtering functionality.
    swiping (SwipingView): Handles swiping functionality.
    """

    def __init__(self, username) -> None:
        """
        Initializes MainMenuView with the username and instances of FilterView and SwipingView.

        Attributes:
        username (str): Username of the logged-in user.
        filter (FilterView): Manages filtering logic.
        swiping (SwipingView): Manages swiping logic.
        """
        self.username = username
        self.filter = FilterView()
        self.swiping = SwipingView()
    
    def show_menu(self):
        """
        Displays the main menu options.
        """
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
            self.show_menu()
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
                edit_view = EditProfileView(self.username)
                edit_view.display_edit_profile()
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu = MainMenuView("username") 
    main_menu.main_menu()
