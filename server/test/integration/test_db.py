import unittest
from .. import create_app, db
from .db_core import fill_db_direct, retrieve_community, retrieve_user, retrieve_debate, retrieve_arguments


class TestUserModelCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pguser:pguser@127.0.0.1:5432/debateit'
        db.drop_all()
        db.create_all()
        self.ids = fill_db_direct(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveCommunity(self):
        c = retrieve_community(self.ids)
        assert(c.id == 1)

    def test_retrieveUser(self):
        u = retrieve_user(self.ids)
        assert(u.id == 1)

    def test_retrieveDebate(self):
        d = retrieve_debate(self.ids)
        assert(d.id == 1)

    def test_retrieveArgumentsForDebate(self):
        arguments = retrieve_arguments(self.ids)
        for argument in arguments:
            assert(self.ids["arg_ids"].__contains__(argument.id))
        assert(len(arguments) == 2)


if __name__ == '__main__':
    unittest.main()
