from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    app.config.from_pyfile("secrets.py")
    return app


app = create_app()
db = SQLAlchemy(app)
db.init_app(app)


def initialize_db():
    with app.app_context():
        db.metadata.drop_all(bind=db.engine)
        db.metadata.create_all(bind=db.engine)
        db.session.commit()
    return db


initialize_db()

from app import routes
