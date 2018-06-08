from app import app
from flask import render_template
import redis

db = redis.Redis(host="redis", port=6379)
db.set("count", 0)


@app.route("/")
def index():
    db.incr("count", 1)
    return render_template("index.html", count=db.get("count"))


@app.route("/u/<username>")
def print_user(username):
    return username


@app.route("/c/<community_name>")
def print_community(community_name):
    return community_name


@app.route("/login")
def login():
    return render_template("login.html")

