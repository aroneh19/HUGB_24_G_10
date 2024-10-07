import unittest
from app import create_app
from app.models.database import Database

class TestLoginRoute(unittest.TestCase):

    def setUp(self):
        """Set up the test client for the Flask app."""
        # Initialize the Flask app and set up the test client
        self.app = create_app().test_client()
        self.app.testing = True

        # Mock the database by pre-populating it with test users
        self.db = Database()
        self.db.save_users({
            "testuser": {
                "password": "testpass",
                "name": "Test User",
                "age": 30,
                "bio": "A test user",
                "interests": ["coding", "basketball"],
                "location": "TestCity"
            }
        })

    def login_user(self, post_data):
        """Helper method to log in a user via a POST request."""
        return self.app.post("/login", json=post_data)
    
    def logout_user(self):
        """Helper method to log out a user via a POST request."""
        return self.app.post("/logout")

    def test_login_success(self):
        """Test successful login with correct credentials."""
        post_data = {
            "username": "testuser", 
            "password": "testpass"
        }

        response = self.login_user(post_data)

        # Assert response status code and message for successful login
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Login successful", response.data)

    def test_login_failure(self):
        """Test login failure with incorrect credentials."""
        post_data = {
            "username": "wronguser", 
            "password": "wrongpass"
        }

        response = self.login_user(post_data)

        # Assert response status code and error message for failed login
        self.assertEqual(response.status_code, 401)
        self.assertIn(b"invalid username or password", response.data)

    def tearDown(self):
        """Clean up the mock database after each test."""
        self.db.save_users({})  # Clear the mock database

if __name__ == "__main__":
    unittest.main()