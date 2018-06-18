from app import app
from flask_sqlalchemy import SQLAlchemy
from .models import User


db = SQLAlchemy(app)


def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    app.logger.info(user)
    app.logger.info(user.name)
    return user
