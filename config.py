import os


class Config(object):
    DEBUG = os.environ.get("FLASK_DEBUG") or False
