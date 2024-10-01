import json

class User:
    def __init__(self, username: str, password: str, fullname: str, 
                 bio: str, interests: list[str], location: str):
        
        self.username = username
        self.password = password
        
        self.fullname = fullname
        self.bio = bio
        self.interests = interests
        self.location = location
    
    def to_json(self):
        """Convert the user to a json string."""
        return json.dumps(self.__dict__)

def load_user(path="data/users.json"):
    """Load all users from the json file."""
    with open(path, 'r') as file:
        users = json.load(file)
    return [User(**user) for user in users]

def save_user(users, path="data/users.json"):
    """Save all users to the json file."""
    with open(path, 'w') as file:
        json.dump([user.__dict__ for user in users], file)

def add_user(username, password, name, bio="", interests="", location=""):
    """Add a user to the json file."""
    users = load_user()
    users.append(User(username, password, name, bio, interests, location))
    save_user(users)