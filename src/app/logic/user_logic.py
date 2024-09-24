from server import SystemInterface
class UserLogic:
    def init(self):
        self.user_storage = {}

    def check_username(self, username):
        try:
            if username in self.user_storage:
                return False
            return True
        except ValueError:
            return False

    def check_age(self, age):
        try:
            if int(age) < 0 or int(age) > 100: # TODO: Check if integer
                return False
            return True
        except ValueError:
            return False

    def check_interests(self, interests):
        if isinstance(interests, list) and len(interests) > 0:
            return True
        return False

    def check_location(self, location):
        try:
            if location == "":
                return False
            return True
        except ValueError:
            return False

    def check_bio(self, bio):
        try:
            if bio == "":
                return False
        except ValueError:
            return True

    def create_user(self, username, password, name, age, bio, interests, location):
        try:
            if self.check_username(username) and self.check_age(age) and self.check_interests(interests) and self.check_location(location) and self.check_bio(bio):
                self.user_storage[username] = {"password": password, "name": name, "age": age, "bio": bio, "interests": interests, "location": location}
                return True
            return False
        except ValueError:
            return False


user = UserLogic()
print(user.check_username("aron")) # True
print(user.check_age(1.2)) # True
print(user.check_interests(["football"])) # True