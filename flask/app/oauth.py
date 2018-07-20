from google.oauth2 import id_token
from google.auth.transport.requests import Request
from app import app


def receive_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(
            token,
            Request(),
            app.config["GOOGLE_LOGIN_CLIENT_ID"]
            )

        if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
            raise ValueError("Wrong issuer")

        user = dict(
            user_id=idinfo["sub"],
            user_email=idinfo["email"],
            user_name=idinfo["name"]
        )

        app.logger.info("User info from google: {}".format(user))
        return user
    except ValueError:
        pass
