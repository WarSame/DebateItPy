from app import app
from flask import render_template
from .forms import EmailPasswordForm
import redis

db = redis.Redis(host="redis", port=6379)
db.set("count", 0)


@app.route("/")
def index():
    db.incr("count", 1)
    count = db.get("count")
    user = db.get("user")
    return render_template("index.html", count=int(count), user=user)


@app.route("/u/<username>")
def print_user(username):
    return username


@app.route("/c/<community_name>")
def print_community(community_name):
    return community_name


@app.route("/login", methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        db.set("user", form.email)
        return render_template("index.html")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    db.delete("user")
    return "logout"
