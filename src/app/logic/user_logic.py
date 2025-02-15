from app.models.database import Database
from app.models.user_model import User


class UserLogic:
    def __init__(self):
        self.db = Database()
        self.current_user = None  # Initialize current_user here
    
    def verify_user(self, username, password):
        """
        Verify if the provided username and password match a user in the database.

        Parameters:
        username (str): The username to verify.
        password (str): The password to verify.

        Returns:
        tuple: A tuple containing a boolean indicating success or failure and a message.
        """
        user_storage = self.db.load_users()  # Load users from the database
        for user in user_storage:
            if user.get("username") == username:
                if user.get("password") == password:  # Check the password
                    self.set_current_user(username)  # Set the current user
                    return True, user
                else:
                    return False, "Invalid password."
        return False, "Username not found."


    def set_current_user(self, username):
        """Set the current user by finding them in the user storage."""
        user_storage = self.db.load_users()
        for user in user_storage:
            if user.get("username") == username:
                self.current_user = user
                break

    def check_username(self, username, user_storage):
        """
        Check if username is available.

        Parameters:
        username (str): The username to check.
        user_storage (list): The list of existing users.

        Returns:
        tuple: A tuple containing a boolean indicating the availability of the username and a message.
        """
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

    def create_user(self, username, password, fullname, age, bio, interests, city, coordinates):
        """
        Create a new user and save to the database.

        Parameters:
        username (str): The username of the user.
        password (str): The password of the user.
        fullname (str): The full name of the user.
        age (int): The age of the user.
        bio (str): The bio of the user.
        interests (list): The interests of the user.
        location (str): The location of the user.
        coordinates (dict): The coordinates of the user's location.

        Returns:
        tuple: A tuple containing a boolean indicating the success of the operation and a message.
        """
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

        valid_location, msg = self.check_location(city)
        if not valid_location:
            return False, msg

        valid_bio, msg = self.check_bio(bio)
        if not valid_bio:
            return False, msg
        
        location = {"city": city, "coordinates": coordinates}

        new_user = User(username, password, fullname, bio, interests, location)
        user_storage.append(new_user.to_dict())
        self.db.save_users(user_storage)

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
