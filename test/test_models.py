from app import app, create_app, initialize_db
import unittest
from app.models import User, Community, Debate, Post


class testUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.db = initialize_db()
        self.app.testing = True

    def test_user(self):
        User.create(name="tedds", email="that@that.com")

    def test_community(self):
        Community.create(name="mysdssdcommunity")


if __name__ == "__main__":
    unittest.main()
