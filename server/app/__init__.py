from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_cors import CORS
from redis import Redis
from config import Config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
redis = Redis(host="redis", port=6379)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .models import Debate, Argument, User, Community

    db.init_app(app)

    migrate.init_app(app, db)
    ma.init_app(app)
    CORS(app)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
