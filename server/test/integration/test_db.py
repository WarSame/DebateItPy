import unittest
from .. import create_app, db, models
from .db_core import fill_db


class TestUserModelCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pguser:pguser@127.0.0.1:5432/debateit'
        db.drop_all()
        db.create_all()
        self.ids = fill_db(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveCommunity(self):
        c = models.Community.retrieve_one(id=self.ids["community_id"])
        assert(c.id == 1)

    def test_retrieveUser(self):
        u = models.User.retrieve_one(id=self.ids["user_id"])
        assert(u.id == 1)

    def test_retrieveDebate(self):
        d = models.Debate.retrieve_one(id=self.ids["debate_id"])
        assert(d.id == 1)

    def test_retrieveArgumentsForDebate(self):
        arguments = models.Argument.retrieve_all(debate_id=self.ids["debate_id"])
        for argument in arguments:
            assert(self.ids["arg_ids"].__contains__(argument.id))
        assert(len(arguments) == 2)


if __name__ == '__main__':
    unittest.main()
