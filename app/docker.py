import os


def info():
    debug = "DEBUG is {}".format( os.environ.get( "DEBUG" ) )
    flask_env = "FLASK_ENV is {}".format( os.environ.get( "FLASK_ENV" ) )
    port = "PORT is {}".format( os.environ.get( "PORT" ) )
    return debug + "\n" + flask_env + "\n" + port
