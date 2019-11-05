import unittest

from .. import create_app, db
from flask import json

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
        db.session.remove()
        db.drop_all()

    def test_get_missing_user(self):
        response = self.app.get('/api/u/1', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_get_existing_user(self):
        post_response = self.app.post(
            '/api/u/',
            data=json.dumps({"name": "Graeme", "email": "graemecliffe@test.com"}),
            content_type="application/json"
        )
        id = json.loads(post_response.data)["id"]
        get_response = self.app.get('/api/u/{}'.format(id), follow_redirects=True)
        self.assertEqual(get_response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
