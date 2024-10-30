from app.logic.filter_logic import FilterLogic

class SwipingView:
    """
    View responsible for displaying and handling swiping functionality.

    Attributes:
    filter_logic (FilterLogic): Handles filtering logic.
    filtered_users (list): Stores the list of users filtered based on criteria.
    """

    def __init__(self, system_interface, current_user) -> None:
        """
        Initializes SwipingView with an instance of FilterLogic.
        """
        self.filter_logic = FilterLogic()
        self.system_interface = system_interface 
        self.current_user = current_user
        self.filtered_users = []

    def start_swiping(self, filters):
        """
        Applies filters and starts the swiping process.
        
        Args:
        filters (dict): Filter criteria to apply when swiping.
        """
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
                self.system_interface.log_swipe_action(self.current_user, user["username"], "like")
                print(f"You liked {user['fullname']}!")
                current_user_index += 1
            elif choice == "l":
                self.system_interface.log_swipe_action(self.current_user, user["username"], "pass")
                print(f"You passed on {user['fullname']}.")
                current_user_index += 1
            elif choice == "b":
                break
            else:
                print("Invalid choice, try again.")

    def display_user(self, user):
        """
        Displays the details of a user during the swiping process.
        
        Args:
        user (dict): The user whose details are to be displayed.
        """
        print(f"Name: {user['fullname']}")
        print(f"Age: {user['age']}")
        print(f"Location: {user['location']}")
        print(f"Interests: {', '.join(user['interests'])}")
        print(f"Bio: {user['bio']}")
        print("---------------------------")
