import unittest
from .. import create_app, db
from .api_core import fill_db_api, retrieve_community, retrieve_user, retrieve_debate, retrieve_arguments


class TestUserModelCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pguser:pguser@127.0.0.1:5432/debateit'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.ids = fill_db_api(self.app)

        self.assertEqual(app.debug, False)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveCommunity(self):
        c = retrieve_community(self.app, self.ids)
        assert (c.json["id"] == 1)

    def test_retrieveUser(self):
        u = retrieve_user(self.app, self.ids)
        assert (u.json["id"] == 1)

    def test_retrieveDebate(self):
        d = retrieve_debate(self.app, self.ids)
        assert (d.json["id"] == 1)

    def test_retrieveArgumentsForDebate(self):
        arguments = retrieve_arguments(self.app, self.ids).json["args"]
        for argument in arguments:
            assert (self.ids["arg_ids"].__contains__(argument.id))
        assert (len(arguments) == 2)


if __name__ == '__main__':
    unittest.main()
