from app import create_app, initialize_db
import unittest
from app.models import User, Community, Debate, Post


class testUser(unittest.TestCase):
    USER_NAME = "tessdddsf"

    def setUp(self):
        self.app = create_app()
        self.db = initialize_db()
        self.app.testing = True

    def test_user_create(self):
        User.create(name=self.USER_NAME, email="that@that.com")

    def test_community_create(self):
        Community.create(name="mysdssdcommunity")

    def test_find_user_by_name(self):
        user = User.retrieve_one(name=self.USER_NAME)

    def test_find_user_by_googleid(self):
        User.create(name="googleuser", email="googleuser@gmail.com", google_id="113431480376190007245")


if __name__ == "__main__":
    unittest.main()
