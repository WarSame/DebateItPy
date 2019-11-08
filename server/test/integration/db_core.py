from .. import models


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


def fill_db(db):
    ids = {
        "user_id": insert_user(db=db),
        "community_id": insert_community(db=db)
    }
    ids["debate_id"] = insert_debate(db=db, c_id=ids["community_id"], u_id=ids["user_id"])
    ids["arg_ids"] = insert_arguments(db=db, d_id=ids["debate_id"], u_id=ids["user_id"])
    return ids
