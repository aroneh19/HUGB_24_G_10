from app.models.database import Database

class UserLogic:
    def __init__(self):
        self.db = Database()

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

    def create_user(self, username, password, name, age, bio, interests, location):
        """Create a new user and save to the database."""
        user_storage = self.db.load_users()

        # Perform checks on new user data
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

        # If all checks pass, add the new user to the list
        new_user = {
            "username": username,
            "password": password,
            "name": name,
            "age": int(age),
            "bio": bio,
            "interests": interests,
            "location": location
        }
        user_storage.append(new_user)

        # Save updated users back to the JSON file
        self.db.save_users(user_storage)

        return True, "User created successfully!"
    
    def edit_username(self, new_username):
        """Edit the username of the current user."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["username"] = new_username
                self.current_user["username"] = new_username
                self.db.save_users(user_storage)
                break
        
    def edit_password(self, new_password):
        """Edit the password of the current user."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["password"] = new_password
                self.db.save_users(user_storage)
                break
    
    def edit_name(self, new_name):
        """Edit the name of the current user."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["name"] = new_name
                self.current_user["name"] = new_name
                self.db.save_users(user_storage)
                break
    
    def edit_age(self, new_age):
        """Edit the age of the current user."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["age"] = int(new_age)
                self.current_user["age"] = int(new_age)
                self.db.save_users(user_storage)
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
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == self.current_user.get("username"):
                user["location"] = new_location
                self.current_user["location"] = new_location
                self.db.save_users(user_storage)
                break
    
