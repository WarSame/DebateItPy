from app import app
import unittest
from app.models import User, Community, Debate, Post


class testUser(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_user(self):
        User.create(name="this", email="that@that.com")

    def test_community(self):
        Community.create(name="mycommunity")


if __name__ == "__main__":
    unittest.main()
