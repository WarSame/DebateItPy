import os


class Config(object):
    DEBUG = os.environ.get('FLASK_DEBUG') or False

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-secret-key'

    GOOGLE_LOGIN_CLIENT_ID = os.environ.get('GOOGLE_LOGIN_CLIENT_ID') or 'some-client-id'
    GOOGLE_LOGIN_CLIENT_SECRET = os.environ.get('GOOGLE_LOGIN_CLIENT_SECRET') or 'some-secret'

    FACEBOOK_LOGIN_CLIENT_ID = os.environ.get('FACEBOOK_LOGIN_CLIENT_ID') or 'some-fb-id'
    FACEBOOK_LOGIN_CLIENT_SECRET = os.environ.get('FACEBOOK_LOGIN_CLIENT_SECRET') or 'some-fb-secret'
