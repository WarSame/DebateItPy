from .db import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    community_id = db.Column(db.Integer, db.ForeignKey('community.id'), nullable=False)
    communities = db.relationship('Community', backref=db.backref('user'))

    def __repr__(self):
        return "<User: {0}>".format(self.name)

    def __init__(self, name):
        self.name = name


class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<Community: {0}>".format(self.name)

    def __init__(self, name):
        self.name = name


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.String(10000), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('post'), uselist=False)

    def __repr__(self):
        return "<Post: {0}>".format(self.title)

    def __init__(self, text):
        self.text = text
