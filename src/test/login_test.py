import unittest
from app.logic.login_logic import LoginLogic

def test_login_success(self):
        """Test successful login."""
        post_data = {
            "username": "testuser", 
            "password": "testpass"
        }

        response = self.login_user(post_data)

        self.assertEqual(response.status_code, 200)

        self.assertIn(b"Login successful", response.data)


def test_login_failure(self):
        """Test login failure with incorrect credentials."""
        post_data = {
            "username": "wronguser", 
            "password": "wrongpass" 
        }

        response = self.login_user(post_data)

        self.assertEqual(response.status_code, 401)

        self.assertIn(b"invalid username or password", response.data)

