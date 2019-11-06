import unittest
from .. import create_app, db, models


class TestUserModelCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pguser:pguser@127.0.0.1:5432/debateit'
        db.drop_all()
        db.create_all()
        self.create_user(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveUser(self):
        u = models.User.retrieve_one(id=self.user_id)
        assert(u.id == 1)

    def create_user(self, db):
        u = models.User(name="graeme", email="graeme@test.com", google_id="something")
        db.session.add(u)
        db.session.commit()
        self.user_id = u.id


if __name__ == '__main__':
    unittest.main()
