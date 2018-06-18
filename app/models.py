from .db import db
from datetime import datetime

user_community_table = db.Table("user_community", db.metadata,
                                db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                                db.Column("community_id", db.Integer, db.ForeignKey("community.id"))
                                )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return "<User: {0}>".format(self.name)


class Community(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<Community: {0}>".format(self.name)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.String(100000), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('post'), uselist=False)

    def __repr__(self):
        return "<Post: {0}>".format(self.title)
