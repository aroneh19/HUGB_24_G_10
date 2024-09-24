import unittest
from app import app

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def create_user(self, post_data):
        """Helper method to create a user via a POST request."""
        return self.app.post("/api/users", json=post_data)

    def test_create_user(self):
        """Test creating a user."""
        post_data = {
            "username": "testuser",
            "password": "testpass",
            "name": "Test User",
            "bio": "This is a test user.",
            "interests": ["coding", "reading"],
            "location": "Reykjavik"
        }
        response = self.create_user(post_data)
        self.assertEqual(response.status_code, 200)
