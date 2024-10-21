from app.models.database import Database

class LoginLogic:
    def __init__(self):
        self.db = Database()
        self.logged_in_users = {}

    def verify_user(self, username, password):
    # Load users from the database
        user_storage = self.db.load_users()

    # user_storage is a list, so we need to loop through it
        for user in user_storage:
            if user['username'] == username:
            # Check if the password matches
                if user['password'] == password:
                # If login is successful, mark the user as logged in
                    self.logged_in_users[username] = True
                    return True
        return False



    def logout_user(self, username):
        # Check if the user is logged in
        if username in self.logged_in_users:
            # Remove user from logged-in state
            del self.logged_in_users[username]
            return True, "User logged out"
        return False, "User was not logged in"
