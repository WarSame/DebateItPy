import os


class Config(object):
    DEBUG = os.environ.get("FLASK_DEBUG") or False
    SECRET_KEY = os.environ.get("FORM_SECRET_KEY") or ""
    GOOGLE_LOGIN_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID") or ""
    GOOGLE_LOGIN_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET") or ""
    FACEBOOK_LOGIN_CLIENT_ID = os.environ.get("FACEBOOK_CLIENT_ID") or ""
    FACEBOOK_LOGIN_CLIENT_SECRET = os.environ.get("FACEBOOK_CLIENT_SECRET") or ""
