import unittest

from .. import create_app, db

TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
