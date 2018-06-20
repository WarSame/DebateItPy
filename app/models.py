from .db import db
from datetime import datetime
from app import app

user_community_table = db.Table("user_community",
                                db.metadata,
                                db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                                db.Column("community_id", db.Integer, db.ForeignKey("community.id"))
                                )


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def retrieve(cls, row_id):
        return db.session.query(id=row_id).first()

    def __repr__(self):
        return self.__dict__

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=db.func.now())


class User(BaseModel):
    __tablename__ = "user"
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<User: {0}>".format(self.name)


class Community(BaseModel):
    __tablename__ = "community"
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(1000))

    def __repr__(self):
        return "<Community: {0}>".format(self.name)


class Post(BaseModel):
    __tablename__ = "post"
    title = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.String(100000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('post'), uselist=False)

    def __repr__(self):
        return "<Post: {0}>".format(self.title)
