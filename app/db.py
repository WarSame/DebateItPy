from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

from .models import User, Post, Community

db.create_all()
db.session.commit()


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    app.logger.info(user)
    user.posts = Post.query.filter_by(user_id=user_id).all()
    return user
