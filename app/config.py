import os


DEBUG = os.environ.get("FLASK_DEBUG") or False

SQLALCHEMY_DATABASE_URI = "postgresql://pguser:pguser@db:5432/debateit"
SQLALCHEMY_TRACK_MODIFICATIONS = False
