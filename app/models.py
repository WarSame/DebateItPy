from . import db
from datetime import datetime

user_community_table = db.Table("user_community",
                                db.metadata,
                                db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                                db.Column("community_id", db.Integer, db.ForeignKey("community.id")),
                                extend_existing=True
                                )


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.DateTime, default=datetime.utcnow())
    update_date = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=db.func.now())

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def retrieve(cls, **kwargs):
        return cls.query.filter_by(kwargs)

    @classmethod
    def update(cls, **kwargs):
        cls.query.update(kwargs)
        db.session.commit()
        return kwargs

    @classmethod
    def delete(cls, **kwargs):
        cls.query.delete(kwargs)
        db.session.commit()

    def __repr__(self):
        return self.__dict__


class User(BaseModel):
    __tablename__ = "user"

    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), nullable=False)
    google_id = db.Column(db.String(100))

    def __repr__(self):
        return "<User: {0}>".format(self.name)


class Community(BaseModel):
    __tablename__ = "community"

    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(1000))

    def __repr__(self):
        return "<Community: {0}>".format(self.name)


class Debate(BaseModel):
    __tablename__ = "debate"

    title = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.String(1000000), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship("User", backref=db.backref("debate", cascade="all,delete"), uselist=False)
    community_id = db.Column(db.Integer, db.ForeignKey("community.id"), nullable=False)
    community = db.relationship("Community", backref=db.backref("debate", cascade="all,delete"), uselist=False)

    def __repr__(self):
        return "<Debate: {0}>".format(self.title)


class Post(BaseModel):
    __tablename__ = "post"

    title = db.Column(db.String(1000), nullable=False)
    text = db.Column(db.String(1000000), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('post'), uselist=False)
    debate_id = db.Column(db.Integer, db.ForeignKey("debate.id"), nullable=False)
    debate = db.relationship("Debate", backref=db.backref("post"), uselist=False)

    def __repr__(self):
        return "<Post: {0}>".format(self.title)
