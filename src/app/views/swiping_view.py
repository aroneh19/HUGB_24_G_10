from app.models.user_model import User

class SwipingView:
    def __init__(self):
        # Hardcoded users for testing
        self.profiles = [
            User("johndoe", "password123", "John Doe", 
                 "I am a test user.", ["Hiking", "Reading"], "New York"),
            User("janedoe", "password456", "Jane Doe", 
                 "Love cooking and movies.", ["Cooking", "Movies"], "Los Angeles"),
            User("bobsmith", "password789", "Bob Smith", 
                 "I enjoy playing video games.", ["Gaming", "Tech"], "Chicago")
        ]
        self.index = 0  
    
    def start_swiping(self):
        """Initiates the swiping process."""
        while self.index < len(self.profiles):
            current_profile = self.profiles[self.index]
            self.display_profile(current_profile)
            
            action = input("Swipe right (1) to like, left (2) to skip, or 'b' to quit: ").lower()
            if action == "1":
                print(f"You liked {current_profile.name}")
            elif action == "2":
                print(f"You skipped {current_profile.name}")
            elif action == "b":
                break
            else:
                print("Invalid input.")
            
            self.index += 1
        
        print("No more profiles to swipe!")
        

    def display_profile(self, profile):
        """Display the current profile in a readable format."""
        print("\n--- Profile ---")
        print(f"Name: {profile.name}")
        print(f"Location: {profile.location}")
        print(f"Interests: {', '.join(profile.interests)}")
        print(f"Bio: {profile.bio}")