import random
from app.logic.filter_logic import FilterLogic

class SwipingView:
    """
    View responsible for displaying and handling swiping functionality.

    Attributes:
    filter_logic (FilterLogic): Handles filtering logic.
    system_interface: Provides access to the system's data management and logging.
    """

    def __init__(self, system_interface, current_user) -> None:
        """
        Initializes SwipingView with an instance of FilterLogic.
        """
        self.filter_logic = FilterLogic()
        self.system_interface = system_interface
        self.current_user = current_user

    def start_swiping(self, filters):
        """
        Applies filters, excludes the current user, previously swiped users, and randomizes the list.
        
        Args:
        filters (dict): Filter criteria to apply when swiping.
        """
        # Get the full filtered user list
        all_filtered_users = self.filter_logic.apply_filters(filters)

        # Load previously swiped users for the current user
        swipes = self.system_interface.db.load_data(self.system_interface.db.swipes_file)
        liked_users = set(swipes.get(self.current_user, {}).get("liked", []))
        passed_users = set(swipes.get(self.current_user, {}).get("passed", []))
        swiped_users = liked_users.union(passed_users)

        # Filter out the current user and previously swiped users
        self.filtered_users = [
            user for user in all_filtered_users 
            if user["username"] != self.current_user and user["username"] not in swiped_users
        ]

        # Randomize the filtered user list
        random.shuffle(self.filtered_users)

        if not self.filtered_users:
            print("No new users found based on your filters.")
            return
        
        # Start the swiping process
        current_user_index = 0
        while current_user_index < len(self.filtered_users):
            user = self.filtered_users[current_user_index]
            self.display_user(user)
            choice = input("Swipe right (r) to like, left (l) to pass, or back (b) to exit swiping: ")

            if choice == "r":
                # Check for match when user swipes right
                match_found = self.system_interface.log_swipe_action(self.current_user, user["username"], "like")
                if match_found:
                    print(f"It's a match! You and {user['fullname']} have liked each other!")
                else:
                    print(f"You liked {user['fullname']}.")
                current_user_index += 1
            elif choice == "l":
                self.system_interface.log_swipe_action(self.current_user, user["username"], "pass")
                print(f"You passed on {user['fullname']}.")
                current_user_index += 1
            elif choice == "b":
                print("Exiting swiping.")
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
        print(f"Location: {user['location']['city']}")
        print(f"Interests: {', '.join(user['interests'])}")
        print(f"Bio: {user['bio']}")
        print("---------------------------")
