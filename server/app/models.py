from flask import current_app
from . import db
from datetime import datetime


user_community_table = db.Table("Users_communities",
                                db.metadata,
                                db.Column("user_id", db.Integer, db.ForeignKey("Users.id")),
                                db.Column("community_id", db.Integer, db.ForeignKey("Communities.id")),
                                extend_existing=True
                                )


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}

    id = db.Column(
        db.Integer,
        primary_key=True
        )
    create_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
        )
    update_date = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        index=True,
        onupdate=db.func.now()
        )

    @classmethod
    def create(cls, **kwargs):
        current_app.logger.info('Creating {} with args: {}'.format(cls.__name__, kwargs))
        obj = cls(**kwargs)
        db.session.add(obj)
        db.session.commit()
        return obj

    @classmethod
    def retrieve_one(cls, **kwargs):
        current_app.logger.info('Retrieving one of {} with args: {}'.format(cls.__name__, kwargs))
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def retrieve_some(cls, n, **kwargs):
        current_app.logger.info('Retrieving {} of {} with args: {}'.format(n, cls.__name__, kwargs))
        return cls.query.filter_by(**kwargs).limit(n).all()

    @classmethod
    def retrieve_all(cls, **kwargs):
        current_app.logger.info('Retrieving all of {} with args: {}'.format(cls.__name__, kwargs))
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def update(cls, **kwargs):
        current_app.logger.info('Updating {} with args: {}'.format(cls.__name__, kwargs))
        cls.query.update(**kwargs)
        db.session.commit()
        return kwargs

    @classmethod
    def delete(cls, **kwargs):
        current_app.logger.info('Deleting {} with args: {}'.format(cls.__name__, kwargs))
        cls.query.delete(**kwargs)
        db.session.commit()

    def __repr__(self):
        return self.__dict__


class User(BaseModel):
    __tablename__ = "Users"

    name = db.Column(
        db.String(80),
        unique=True,
        nullable=False
        )
    email = db.Column(
        db.String(80),
        nullable=False
        )
    google_id = db.Column(
        db.String(100)
        )
    debates = db.relationship(
        "Debate",
        backref="creator",
        lazy="dynamic"
    )

    def __repr__(self):
        return "<User: {0}>".format(self.name)


class Community(BaseModel):
    __tablename__ = "Communities"

    name = db.Column(
        db.String(80),
        unique=True,
        nullable=False
        )
    description = db.Column(
        db.String(1000)
        )
    debates = db.relationship(
        "Debate",
        backref="community",
        lazy="dynamic"
    )

    def __repr__(self):
        return "<Community: {0}>".format(self.name)


class Debate(BaseModel):
    __tablename__ = "Debates"

    title = db.Column(
        db.String(1000),
        nullable=False
        )
    description = db.Column(
        db.String(10000),
        nullable=True
    )
    creator_id = db.Column(
        db.Integer,
        db.ForeignKey("Users.id"),
        nullable=False
        )
    community_id = db.Column(
        db.Integer,
        db.ForeignKey("Communities.id"),
        nullable=False
        )
    arguments = db.relationship(
        "Argument",
        backref="debate",
        lazy="dynamic"
    )

    def __repr__(self):
        return "<Debate: {0}>".format(self.title)


class Argument(BaseModel):
    __tablename__ = "Arguments"

    title = db.Column(
        db.String(1000),
        nullable=False
        )
    content = db.Column(
        db.String(1000000),
        nullable=False
        )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('Users.id'),
        nullable=False
        )
    debate_id = db.Column(
        db.Integer,
        db.ForeignKey('Debates.id'),
        nullable=False
        )

    def __repr__(self):
        return "<Argument: {0}>".format(self.title)
