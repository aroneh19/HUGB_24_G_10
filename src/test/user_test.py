import unittest
from app.logic.user_logic import UserLogic

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_logic = UserLogic()

    def test_check_username(self):
        self.assertTrue(self.user_logic.check_username("new_user"))
        self.user_logic.user_storage["existing_user"] = {}
        self.assertFalse(self.user_logic.check_username("existing_user"))

    def test_check_age(self):
        self.assertTrue(self.user_logic.check_age(25))
        self.assertFalse(self.user_logic.check_age(-1))
        self.assertFalse(self.user_logic.check_age(150))
        self.assertFalse(self.user_logic.check_age("invalid_age"))

    def test_check_interests(self):
        self.assertTrue(self.user_logic.check_interests(["basketball", "coding"]))
        self.assertFalse(self.user_logic.check_interests([]))
        self.assertFalse(self.user_logic.check_interests("not a list"))

    def test_check_location(self):
        self.assertTrue(self.user_logic.check_location("Reykjavik"))
        self.assertFalse(self.user_logic.check_location(""))

    def test_check_bio(self):
        self.assertTrue(self.user_logic.check_bio("I love sports"))
        self.assertFalse(self.user_logic.check_bio(""))

    def test_create_user(self):
        result = self.user_logic.create_user(
            "jon_doe", "password123", "Jon Doe", 30, 
            "I enjoy basketball", ["basketball", "coding"], "Reykjavik"
        )
        self.assertTrue(result)
        self.assertIn("jon_doe", self.user_logic.user_storage)

        result = self.user_logic.create_user(
            "jane_doe", "password123", "Jane Doe", -5,
            "I enjoy running", ["running"], "Akureyri"
        )
        self.assertFalse(result)
        self.assertNotIn("jane_doe", self.user_logic.user_storage)

if __name__ == "__main__":
    unittest.main()
