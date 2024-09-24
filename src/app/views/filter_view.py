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
        pass

    def filter_location(self):
        pass