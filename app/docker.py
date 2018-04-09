import os


def info():
    debug = "DEBUG is {}".format( os.environ.get( "DEBUG" ) )
    return debug
