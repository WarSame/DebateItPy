import psycopg2.extras
from app import app


conn = psycopg2.connect(dbname="debateit", host="db", port=5432, user="pguser", password="pguser")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def create_user(name):
    cur.execute("INSERT INTO users (name) VALUES (%s)", name)


def get_user(userid):
    cur.execute("SELECT * from users;")
    user = cur.fetchone()
    app.logger.info(user)
    return user
