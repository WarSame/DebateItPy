import unittest
from .. import app, db
from .. import User, Post

class TestUserModelCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        self.create_user(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveUser(self):
        u = User.retrieve_one(id=user_id)
        assert(5==4)

    def create_user(db):
        u = User(name="graeme", email="graeme@test.com", google_id="something")
        db.session.add(u)
        db.session.commit()
        user_id = u.id

if __name__ == '__main__':
    unittest.main()
