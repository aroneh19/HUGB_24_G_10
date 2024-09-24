import sys
from app.server.interface import SystemInterface
from app.views.filter_view import FilterView
from app.views.profile_view import ProfileView
from app.views.swiping_view import SwipingView

class MainMenuView:
    def __init__(self) -> None:
        self.iface = SystemInterface()
        self.filter = FilterView()
        self.swiping = SwipingView()
    
    def show_menu(self):
        print("1. Start Swiping")
        print("2. Filter")
        print("3. Messages")
        print("4. Profile")

    def main_menu(self):
        while True:
            self.show_menu()
            choice = input("Enter choice: ")
            if choice == "1":
                self.swiping.start_swiping()
            elif choice == "2":
                self.filter.set_filter()
            elif choice == "3":
                print("Messages")
            elif choice == "4":
                print("Profile")
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu = MainMenuView()
    main_menu.main_menu()