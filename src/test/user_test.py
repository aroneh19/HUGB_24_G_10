import unittest
from app.logic.user_logic import UserLogic
from app.logic.location_logic import LocationLogic

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_logic = UserLogic()
        self.location_logic = LocationLogic()

    def test_check_username(self):
        self.assertTrue(self.user_logic.check_username("new_user", self.user_logic.user_storage)[0])
        self.user_logic.user_storage["existing_user"] = {}
        self.assertFalse(self.user_logic.check_username("existing_user", self.user_logic.user_storage)[0])

    def test_check_age(self):
        self.assertTrue(self.user_logic.check_age(25)[0])
        self.assertFalse(self.user_logic.check_age(-1)[0])
        self.assertFalse(self.user_logic.check_age(150)[0])
        self.assertFalse(self.user_logic.check_age("invalid_age")[0])

    def test_check_interests(self):
        self.assertTrue(self.user_logic.check_interests(["basketball", "coding"])[0])
        self.assertFalse(self.user_logic.check_interests([])[0])
        self.assertFalse(self.user_logic.check_interests("not a list")[0])

    def test_check_location(self):
        self.assertTrue(self.user_logic.check_location("Reykjavik")[0])
        self.assertFalse(self.user_logic.check_location("")[0])

    def test_check_bio(self):
        self.assertTrue(self.user_logic.check_bio("I love sports")[0])
        self.assertFalse(self.user_logic.check_bio("")[0])

    def test_create_user(self):
        coordinates = self.location_logic.get_location_coordinates("Reykjavik")
        result = self.user_logic.create_user(
            "jon_doe", "password123", "Jon Doe", 30, 
            "I enjoy basketball", ["basketball", "coding"], "Reykjavik", coordinates
        )
        self.assertTrue(result)

        coordinates = self.location_logic.get_location_coordinates("Akureyri")
        result = self.user_logic.create_user(
            "jane_doe", "password123", "Jane Doe", -5,
            "I enjoy running", ["running"], "Akureyri", coordinates
        )
        self.assertFalse(result)
        self.assertNotIn("jane_doe", self.user_logic.user_storage)
    
    def test_create_user_with_existing_username(self):
        coordinates = self.location_logic.get_location_coordinates("Reykjavik")
        self.user_logic.create_user("john_doe", "password", "John Doe", 30, "I like soccer", ["soccer"], "Reykjavik", coordinates)
        result, msg = self.user_logic.create_user("john_doe", "newpassword", "Johnathan Doe", 25, "I love tennis", ["tennis"], "Reykjavik", coordinates)
        self.assertFalse(result)
        self.assertEqual(msg, "Username already taken.")


if __name__ == "__main__":
    unittest.main()
