import unittest
from app.logic.filter_logic import FilterLogic

class MockDatabase:
    def load_users(self):
        return [
            {"username": "jonatan", "age": 24, "location": "Reykjavik", "interests": ["Sports", "Fitness", "Music"]},
            {"username": "hrefna", "age": 29, "location": "Akureyri", "interests": ["Books", "Art", "Photography"]},
            {"username": "jonas", "age": 18, "location": "Keflavik", "interests": ["Gaming", "Movies", "Technology"]}
        ]

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.filter_logic = FilterLogic()
        self.filter_logic.db = MockDatabase()

    def test_filter_by_interests(self):
        filters = {"interests": ["Sports"], "age": None, "location": None}
        result = self.filter_logic.apply_filters(filters)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['username'], "jonatan")

    def test_filter_by_age(self):
        filters = {"interests": [], "age": (20, 30), "location": None}
        result = self.filter_logic.apply_filters(filters)
        self.assertEqual(len(result), 2)
        self.assertIn("jonatan", [user['username'] for user in result])
        self.assertIn("hrefna", [user['username'] for user in result])

    def test_filter_by_location(self):
        filters = {"interests": [], "age": None, "location": "Keflavik"}
        result = self.filter_logic.apply_filters(filters)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['username'], "jonas")

    def test_combined_filters(self):
        filters = {"interests": ["Gaming"], "age": (15, 25), "location": "Keflavik"}
        result = self.filter_logic.apply_filters(filters)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['username'], "jonas")

    def test_no_filters(self):
        filters = {"interests": [], "age": None, "location": None}
        result = self.filter_logic.apply_filters(filters)
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
