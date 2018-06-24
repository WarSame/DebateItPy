from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


def initialize_db():
    db.init_app(app)
    with app.app_context():
        db.metadata.drop_all(bind=db.engine)
        db.metadata.create_all(bind=db.engine)
        db.session.commit()


from app import routes
