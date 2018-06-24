from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile("config.py")
app.config.from_pyfile("secrets.py")

db = SQLAlchemy(app)


def initialize_db():
    db.init_app(app)
    with app.app_context():
        db.metadata.drop_all(bind=db.engine)
        db.metadata.create_all(bind=db.engine)
        db.session.commit()


from app import routes
