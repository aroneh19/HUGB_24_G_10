import unittest
from unittest.mock import patch
from app.logic.user_logic import UserLogic

class TestCreateProfile(unittest.TestCase):

    def setUp(self):
        """Set up the test logic for creating a profile."""
        self.user_logic = UserLogic()

        # Mock the database storage with test users
        self.mock_users = [
            {
                "username": "existinguser",
                "password": "password123",
                "name": "John Doe",
                "age": 25,
                "bio": "I love coding.",
                "interests": ["coding", "gaming"],
                "location": {
                    "city": "Reykjavík",
                    "coordinates": {
                        "longitude": -21.9422367,
                        "latitude": 64.145981
                    }
                }
            }
        ]

        # Patch the database's load_users and save_users methods
        patcher = patch('app.models.database.Database.load_users', return_value=self.mock_users)
        self.mock_load_users = patcher.start()
        self.addCleanup(patcher.stop)

        patcher_save = patch('app.models.database.Database.save_users')
        self.mock_save_users = patcher_save.start()
        self.addCleanup(patcher_save.stop)

    def test_create_user_success(self):
        """Test successful creation of a new user."""
        username = "newuser"
        password = "newpass123"
        name = "Jane Doe"
        age = 28
        bio = "I enjoy hiking and reading."
        interests = ["hiking", "reading"]
        location = "Los Angeles"
        coordinates = {"latitude": 34.0522, "longitude": -118.2437}  # Example coordinates

        # Call the user logic create_user function
        success, message = self.user_logic.create_user(username, password, name, age, bio, interests, location, coordinates)

        # Assert successful profile creation
        self.assertTrue(success)
        self.assertEqual(message, "User created successfully!")
        self.mock_save_users.assert_called_once()  # Ensure save_users is called once

    def test_create_user_username_taken(self):
        """Test creating a user with a username that's already taken."""
        username = "existinguser"  # Username already in mock_users
        password = "newpass123"
        name = "Jane Doe"
        age = 28
        bio = "I enjoy hiking and reading."
        interests = ["hiking", "reading"]
        location = "Los Angeles"
        coordinates = {"latitude": 34.0522, "longitude": -118.2437}  # Example coordinates

        success, message = self.user_logic.create_user(username, password, name, age, bio, interests, location, coordinates)

        # Assert that the creation fails due to taken username
        self.assertFalse(success)
        self.assertEqual(message, "Username already taken.")
        self.mock_save_users.assert_not_called()  # Ensure save_users was not called

    def test_create_user_invalid_age(self):
        """Test creating a user with an invalid age."""
        username = "newuser"
        password = "newpass123"
        name = "Jane Doe"
        age = "invalid_age"  # Invalid age input (non-integer)
        bio = "I enjoy hiking and reading."
        interests = ["hiking", "reading"]
        location = "Los Angeles"
        coordinates = {"latitude": 34.0522, "longitude": -118.2437}  # Example coordinates

        success, message = self.user_logic.create_user(username, password, name, age, bio, interests, location, coordinates)

        # Assert failure due to invalid age
        self.assertFalse(success)
        self.assertEqual(message, "Age must be an integer.")
        self.mock_save_users.assert_not_called()  # Ensure save_users was not called

    def test_create_user_empty_bio(self):
        """Test creating a user with an empty bio."""
        username = "newuser"
        password = "newpass123"
        name = "Jane Doe"
        age = 28
        bio = ""  # Empty bio
        interests = ["hiking", "reading"]
        location = "Los Angeles"
        coordinates = {"latitude": 34.0522, "longitude": -118.2437}  # Example coordinates

        success, message = self.user_logic.create_user(username, password, name, age, bio, interests, location, coordinates)

        # Assert failure due to empty bio
        self.assertFalse(success)
        self.assertEqual(message, "Bio cannot be empty.")
        self.mock_save_users.assert_not_called()  # Ensure save_users was not called

    def test_create_user_no_interests(self):
        """Test creating a user without specifying interests."""
        username = "newuser"
        password = "newpass123"
        name = "Jane Doe"
        age = 28
        bio = "I enjoy hiking and reading."
        interests = []  # No interests
        location = "Los Angeles"
        coordinates = {"latitude": 34.0522, "longitude": -118.2437}  # Example coordinates

        success, message = self.user_logic.create_user(username, password, name, age, bio, interests, location, coordinates)

        # Assert failure due to empty interests
        self.assertFalse(success)
        self.assertEqual(message, "Interests must be a non-empty list.")
        self.mock_save_users.assert_not_called()  # Ensure save_users was not called

    def test_create_user_invalid_location(self):
        """Test creating a user with an invalid location (empty string)."""
        username = "newuser"
        password = "newpass123"
        name = "Jane Doe"
        age = 28
        bio = "I enjoy hiking and reading."
        interests = ["hiking", "reading"]
        location = ""  # Empty location
        coordinates = {"latitude": 34.0522, "longitude": -118.2437}  # Example coordinates

        success, message = self.user_logic.create_user(username, password, name, age, bio, interests, location, coordinates)

        # Assert failure due to empty location
        self.assertFalse(success)
        self.assertEqual(message, "Location cannot be empty.")
        self.mock_save_users.assert_not_called()  # Ensure save_users was not called

    def tearDown(self):
        """Clean up after each test."""
        # Ensure any necessary cleanup after each test case
        pass

if __name__ == "__main__":
    unittest.main()
