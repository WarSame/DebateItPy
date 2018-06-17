import psycopg2.extras
from app import app


conn = psycopg2.connect(dbname="debateit", host="db", port=5432, user="pguser", password="pguser")
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def create_user(name):
    cur.execute("INSERT INTO users (name) VALUES (%s)", name)


def get_user(user_id):
    cur.execute("SELECT * from users WHERE id = %s;", user_id)
    user = cur.fetchone()
    app.logger.info(user)
    return user
