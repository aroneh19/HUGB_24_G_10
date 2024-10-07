class FilterView:
    def __init__(self) -> None:
        self.filter = {
            "interests": [],
            "age": None,
            "location": None
        }

    def filter_menu(self):
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
                    "location": None}
            elif choice == "b":
                break
            else:
                print("Invalid choice, try again.")
    
    def filter_interests(self):
        """Get the interests to filter by."""
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
            if choice == "b":
                break
            self.filter["interests"].append(interests_list[int(choice) - 1])

            print(self.filter)

    def filter_age(self):
        """Get the minimum and maximum age to filter by."""
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
        """Validate the minimum and maximum age, ensuring they are integers and within the valid range."""
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
        pass