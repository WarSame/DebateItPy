import unittest
from app import app, db
from app.models import User, Post

class Test_UserModelCase(unittest.TestCase):
    id = 0
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()
        u = User(name="graeme", email="graeme@test.com", google_id="something")
        db.session.add(u)
        db.session.commit()
        id = u.id

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveUser(self):
        u = User.retrieve_one(id=id)

if __name__ == '__main__':
    unittest.main()
