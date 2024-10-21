import sys
from app.views.filter_view import FilterView
from app.views.swiping_view import SwipingView
from app.views.edit_profile_view import EditProfileView

class MainMenuView:
    def __init__(self, username) -> None:
        self.username = username
        self.filter = FilterView()
        self.swiping = SwipingView()
    
    def show_menu(self):
        print("1. Start Swiping")
        print("2. Filter")
        print("3. Messages")
        print("4. Profile")
        print("5. Edit Profile")

    def main_menu(self):
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
    main_menu = MainMenuView() 
    main_menu.main_menu()