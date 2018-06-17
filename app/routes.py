from app import app
from flask import render_template, redirect
from .forms import EmailPasswordForm
import redis
from .db import conn

redis = redis.Redis(host="redis", port=6379)


@app.route("/")
def index():
    user = redis.get("user")
    if user is None:
        user = ""
    else:
        user = user.decode("utf-8")
    return render_template("index.html", user=user)


@app.route("/u/<username>")
def print_user(username):
    return username


@app.route("/c/<community_name>")
def print_community(community_name):
    return community_name


@app.route("/login", methods=("GET", "POST"))
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        app.logger.info("Posting login")
        redis.set("user", form.email.data)
        return redirect("/")
    app.logger.info("Getting login")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    redis.delete("user")
    return "logout"
