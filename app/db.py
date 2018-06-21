from app import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


def initialize_db():
    db.metadata.drop_all(bind=db.engine)
    db.metadata.create_all(bind=db.engine)
    db.session.commit()
