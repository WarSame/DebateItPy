import os
import configparser


class Config(object):
    DEBUG = os.environ.get("FLASK_DEBUG") or False

    config = configparser.ConfigParser()
    config.read(os.path.abspath("/app/client.secrets"))

    #SECRET_KEY = config.get("forms", "SECRET_KEY")
    #GOOGLE_LOGIN_CLIENT_ID = config.get("google-auth", "GOOGLE_LOGIN_CLIENT_ID")
    #GOOGLE_LOGIN_CLIENT_SECRET = config.get("google-auth", "GOOGLE_LOGIN_CLIENT_SECRET")
    #FACEBOOK_LOGIN_CLIENT_ID = config.get("facebook-auth", "FACEBOOK_LOGIN_CLIENT_ID")
    #FACEBOOK_LOGIN_CLIENT_SECRET = config.get("facebook-auth", "FACEBOOK_LOGIN_CLIENT_SECRET")

    #SQLALCHEMY_DATABASE_URI = "postgresql://pguser:pguser@db:5432/debateit"
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
