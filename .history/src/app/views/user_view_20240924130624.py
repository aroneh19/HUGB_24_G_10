from app.logic.user_logic import UserLogic
class CreateProfileView:
    def __init__(self):
        self.profile = {
            "username": None,
            "password": None,
            "name": None,
            "age": None,
            "bio": None,
            "interests": [],
            "location": None
        }

    def create_profile_menu(self):
        while True:
            print("=== Create a New Profile ===")
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            bio = input("Write a short bio: ")
            interests = self.get_interests()
            location = input("Enter your location: ")

            if self.UserLogic.c(username, password, name, age, bio, interests, location):
                print(f"Profile for {username} created successfully!")
                break
            else:
                print("Failed to create profile. Please try again.")
                print("Check if the username already exists or other information is invalid.")
    
    def get_interests(self):
        print("Please select your interests from the list below:")
        interests_list = [
            "Sports", "Books", "Music", "Movies", "Video Games", "Art", 
            "Cooking", "Fitness", "Travel", "Photography", "Fashion", 
            "Technology", "Science", "Gardening", "Hiking", "Yoga", 
            "Dancing", "Writing", "Meditation", "Gaming"
        ]
        selected_interests = []

        while True:
            for i, interest in enumerate(interests_list, 1):
                print(f"{i}. {interest}")
            print("Type 'b' to finish selecting interests.")

            choice = input("Enter the number of your interest: ")
            if choice == "b":
                if selected_interests:
                    break
                else:
                    print("You must select at least one interest.")
            else:
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(interests_list):
                        selected_interests.append(interests_list[index])
                        print(f"Selected interests: {selected_interests}")
                    else:
                        print("Invalid choice, please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        return selected_interests

# To use the UI:
if __name__ == "__main__":
    create_profile_view = CreateProfileView()
    create_profile_view.create_profile_menu()