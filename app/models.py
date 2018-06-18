from .db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=False)

    def __repr__(self):
        return "<User: {0}>".format(self.username)

    def __init__(self, name):
        self.id = id
        self.name = name