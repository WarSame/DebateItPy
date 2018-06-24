from app import app
import unittest


class testUser(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test(self):
        print("hello")


if __name__ == "__main__":
    unittest.main()
