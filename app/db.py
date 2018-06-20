from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

from .models import *

db.create_all()
db.session.commit()


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    app.logger.info(user)
    return user


def create_user(name):
    user = User(name=name)
    db.session.add(user)
    db.session.commit()
    return user


def create_community(name, description):
    community = Community(name=name, description=description)
    db.session.add(community)
    db.session.commit()
    return community


def get_community(community_id):
    community = Community.query.filter_by(id=community_id).first()
    app.logger.info(community)
    return community


def create_post(title, text, user_id):
    post = Post(title=title, text=text, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return post


def get_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    app.logger.info(post)
    return post
