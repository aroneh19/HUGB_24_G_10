from app.models.database import Database

class UserLogic:
    def __init__(self):
        self.db = Database()
        self.current_user = None  # Initialize current_user here

    def set_current_user(self, username):
        """Set the current user by finding them in the user storage."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == username:
                self.current_user = user
                break

    def check_username(self, username, user_storage):
        """Check if username is available."""
        for user in user_storage:
            if user.get("username") == username:
                return False, "Username already taken."
        return True, None


    def check_age(self, age):
        """Check if age is a valid integer and within acceptable range."""
        try:
            age = int(age)
            if 0 <= age <= 100:
                return True, None
            else:
                return False, "Age must be between 0 and 100."
        except ValueError:
            return False, "Age must be an integer."

    def check_interests(self, interests):
        """Check if interests are valid."""
        if isinstance(interests, list) and len(interests) > 0:
            return True, None
        return False, "Interests must be a non-empty list."

    def check_location(self, location):
        """Check if location is valid (non-empty)."""
        if location.strip() != "":
            return True, None
        return False, "Location cannot be empty."

    def check_bio(self, bio):
        """Check if bio is valid (non-empty)."""
        if bio.strip() != "":
            return True, None
        return False, "Bio cannot be empty."

    def create_user(self, username, password, fullname, age, bio, interests, location, coordinates):
        """Create a new user and save to the database."""
        is_valid, msg = self.validate_user_data(username, age, bio, interests, location)
        if not is_valid:
            return False, msg

        # Create and save the user
        new_user = {
            "username": username,
            "password": password,
            "fullname": fullname,
            "interests": interests,
            "location": {
                "city": location,
                "coordinates": coordinates
            },
            "age": int(age),
            "bio": bio
        }
        user_storage = self.db.load_users()
        user_storage.append(new_user)
        self.db.save_users(user_storage)

        return True, "User created successfully!"
    
    def validate_user_data(self, username, age, bio, interests, location):
        """Validate user data."""
        user_storage = self.db.load_users()

        valid_username, msg = self.check_username(username, user_storage)
        if not valid_username:
            return False, msg

        valid_age, msg = self.check_age(age)
        if not valid_age:
            return False, msg

        valid_interests, msg = self.check_interests(interests)
        if not valid_interests:
            return False, msg

        valid_location, msg = self.check_location(location)
        if not valid_location:
            return False, msg

        valid_bio, msg = self.check_bio(bio)
        if not valid_bio:
            return False, msg

        return True, None

    def set_current_user(self, username):
        """Set the current user by finding them in the user storage."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == username:
                self.current_user = user
                break

    def edit_bio(self, new_bio):
        """Edit the bio of the current user."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["bio"] = new_bio
                self.current_user["bio"] = new_bio
                self.db.save_users(user_storage)
                break
    
    def edit_interests(self, new_interests):
        """Edit the interests of the current user."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["interests"] = new_interests
                self.current_user["interests"] = new_interests
                self.db.save_users(user_storage)
                break

    def edit_location(self, new_location):
        """Edit the location of the current user."""
        # Validate the new location (you already have a method for this)
        valid_location, msg = self.check_location(new_location)
        if not valid_location:
            return False, msg

        # Load user storage and update location
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["location"] = new_location
                self.current_user["location"] = new_location
                self.db.save_users(user_storage)
                return True, "Location updated successfully."

        return False, "User not found."
