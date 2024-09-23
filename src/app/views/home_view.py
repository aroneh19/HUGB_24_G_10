import sys
from app.server.interface import SystemInterface

class MainMenuView:
    def __init__(self) -> None:
        self.iface = SystemInterface()
    
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
                print("Start Swiping")
            elif choice == "2":
                print("Filter")
            elif choice == "3":
                print("Messages")
            elif choice == "4":
                print("Profile")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu = MainMenuView()
    main_menu.main_menu()