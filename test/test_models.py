import debateit
import unittest
from flask_sqlalchemy import SQLAlchemy

class testUser(unittest.TestCase):
    def setUp(self):
        debateit.app.config["SECRET_KEY"] = "this"
        debateit.testing = True
        debateit.db = SQLAlchemy(debateit)
        self.app = debateit.app.test_client()
        with debateit.app.app_context():
            debateit.app.db.initialize_db()

    def test(self):
        print("hello")


if __name__ == "__main__":
    unittest.main()
