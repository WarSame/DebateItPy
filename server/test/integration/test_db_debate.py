import unittest
from .. import create_app, db, models


def insert_user(db):
    u = models.User(name="graeme", email="graeme@test.com", google_id="something")
    db.session.add(u)
    db.session.commit()
    return u.id


def insert_community(db):
    c = models.Community(name="mycommunity", description="something")
    db.session.add(c)
    db.session.commit()
    return c.id


def insert_debate(db, u_id, c_id):
    d = models.Debate(title="somedebate", description="somedescription", creator_id=u_id, community_id=c_id)
    db.session.add(d)
    db.session.commit()
    return d.id


def insert_arguments(db, u_id, d_id):
    arg1 = models.Argument(title="sometitle", content="somecontent", user_id=u_id, debate_id=d_id)
    db.session.add(arg1)
    db.session.commit()
    arg2 = models.Argument(title="sometitle", content="somecontent", user_id=u_id, debate_id=d_id)
    db.session.add(arg2)
    db.session.commit()
    return [arg1.id, arg2.id]


class TestUserModelCase(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        app.testing = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pguser:pguser@127.0.0.1:5432/debateit'
        db.drop_all()
        db.create_all()
        self.fill_db(db)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_retrieveCommunity(self):
        c = models.Community.retrieve_one(id=self.community_id)
        assert(c.id == 1)

    def test_retrieveUser(self):
        u = models.User.retrieve_one(id=self.user_id)
        assert(u.id == 1)

    def test_retrieveDebate(self):
        d = models.Debate.retrieve_one(id=self.debate_id)
        assert(d.id == 1)

    def test_retrieveArguments(self):
        arguments = []
        for id in self.arg_ids:
            arguments.append(models.Argument.retrieve_one(id=id))
        assert(len(arguments) == 2)

    def fill_db(self, db):
        self.user_id = insert_user(db=db)
        self.community_id = insert_community(db=db)
        self.debate_id = insert_debate(db=db, c_id=self.community_id, u_id=self.user_id)
        self.arg_ids = insert_arguments(db=db, d_id=self.debate_id, u_id=self.user_id)


if __name__ == '__main__':
    unittest.main()
