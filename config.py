import os


class Config(object):
    PORT = os.environ.get("PORT") or 5002
    DEBUG = os.environ.get("DEBUG") or True
