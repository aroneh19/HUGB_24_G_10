from app.logic.filter_logic import FilterLogic

class SwipingView:
    def __init__(self) -> None:
        self.filter_logic = FilterLogic()
        self.filtered_users = []

    def start_swiping(self, filters):
        self.filtered_users = self.filter_logic.apply_filters(filters)
        
        if not self.filtered_users:
            print("No users found based on your filters.")
            return
        
        current_user_index = 0
        while current_user_index < len(self.filtered_users):
            user = self.filtered_users[current_user_index]
            self.display_user(user)
            choice = input("Swipe right (r) to like or left (l) to pass (b to go back): ")

            if choice == "r":
                print(f"You liked {user['fullname']}!")
                current_user_index += 1
            elif choice == "l":
                print(f"You passed on {user['fullname']}.")
                current_user_index += 1
            elif choice == "b":
                break
            else:
                print("Invalid choice, try again.")
    
    def display_user(self, user):
        print(f"Name: {user['fullname']}")
        print(f"Age: {user['age']}")
        print(f"Location: {user['location']}")
        print(f"Interests: {', '.join(user['interests'])}")
        print(f"Bio: {user['bio']}")
        print("---------------------------")
