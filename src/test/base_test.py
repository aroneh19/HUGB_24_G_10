import unittest
from app import app

class BaseTest:
    def setup(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def create_user(self, post_data):
        return self.app.post("/api/users", json=post_data)