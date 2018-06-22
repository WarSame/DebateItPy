from google.oauth2 import id_token
from google.auth.transport import requests
from app import app


def receive_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), app.config["GOOGLE_LOGIN_CLIENT_ID"])

        if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
            raise ValueError("Wrong issuer")

        userid = idinfo["sub"]
        app.logger.info("Logging user info from google: {}".format(userid))
        return userid
    except ValueError:
        pass
