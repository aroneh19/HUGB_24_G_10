class FilterView:
    """
    View responsible for filtering user profiles based on interests, age, and location.

    Attributes:
    filter (dict): Stores filter criteria.
    """

    def __init__(self) -> None:
        """
        Initializes FilterView with default filter criteria.

        Attributes:
        filter (dict): Holds interests, age, and location filters.
        """
        self.filter = {
            "interests": [],
            "age": None,
            "location": None
        }

    def filter_menu(self):
        """
        Displays the filter menu and handles user input for setting filter criteria.
        """
        while True:
            print("Filter by:")
            print("-----1. Interests")
            print("-----2. Age")
            print("-----3. Location")
            print("-----c. Clear filters")
            choice = input("Enter choice: ")

            if choice == "1":
                self.filter_interests()
            elif choice == "2":
                self.filter_age()
            elif choice == "3":
                self.filter_location()
            elif choice == "c":
                self.filter = {
                    "interests": [],
                    "age": [],
                    "location": None
                }
            elif choice == "b":
                break
            else:
                print("Invalid choice, try again.")
    
    def filter_interests(self):
        """
        Sets the interests to filter by.
        """
        interests_list = [
            "Sports", "Books", "Music", "Movies", "Video Games", "Art", 
            "Cooking", "Fitness", "Travel", "Photography", "Fashion", 
            "Technology", "Science", "Gardening", "Hiking", "Yoga", 
            "Dancing", "Writing", "Meditation", "Gaming"
        ]

        while True:
            for i, j in enumerate(interests_list, 1):
                print(f"{i}. {j}")

            choice = input("Enter choice: ")
            if choice == "d":
                break
            self.filter["interests"].append(interests_list[int(choice) - 1])

            print(self.filter)

    def filter_age(self):
        """
        Sets the minimum and maximum age to filter by.
        """
        while True:
            min_age = input("Enter minimum age: ")
            max_age = input("Enter maximum age: ")
            valid, result = self.age_validator(min_age, max_age)
            if valid:
                self.filter["age"] = result
                break
            else:
                print(result)
    
    def age_validator(self, min_age, max_age):
        """
        Validates the minimum and maximum age input.

        Args:
        min_age (str): Minimum age as input.
        max_age (str): Maximum age as input.

        Returns:
        tuple: Boolean indicating validity and either a result or an error message.
        """
        try:
            min_age = int(min_age)
            max_age = int(max_age)

            if not (1 <= min_age <= 100):
                return False, "Minimum age must be between 1 and 100."
            if not (1 <= max_age <= 100):
                return False, "Maximum age must be between 1 and 100."
            if min_age > max_age:
                return False, "Minimum age cannot be greater than maximum age."
            return True, (min_age, max_age)
        except ValueError:
            return False, "Invalid input. Ages must be numbers."

    def filter_location(self):
        """
        Sets the location to filter by.
        """
        locations_list = [
            "Reykjavík", "Kópavogur", "Hafnarfjörður", "Akureyri", "Reykjanesbær", 
            "Garðabær", "Mosfellsbær", "Árborg", "Akranes", "Fjarðabyggð", 
            "Hveragerði", "Vestmannaeyjar", "Grindavík", "Seltjarnarnes", "Borgarbyggð", 
            "Höfn", "Egilsstaðir", "Dalvík", "Húsavík", "Selfoss", 
            "Ísafjörður", "Sauðárkrókur", "Siglufjörður", "Bolungarvík", "Vogar"
        ]

        while True:
            for i, location in enumerate(locations_list, 1):
                print(f"{i}. {location}")

            choice = input("Enter choice or 'b' to go back: ")
            if choice == "b":
                break
            if choice.isdigit() and 1 <= int(choice) <= len(locations_list):
                selected_location = locations_list[int(choice) - 1]
                self.filter["location"] = selected_location
                print(f"Location filter set: {self.filter['location']}")
                break
            else:
                print("Invalid choice, try again.")
