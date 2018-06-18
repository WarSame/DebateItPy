from app import app
from flask import render_template, redirect
from .forms import EmailPasswordForm
import redis
from .db import get_user, create_user

redis = redis.Redis(host="redis", port=6379)


@app.route("/")
def index():
    user = redis.get("user")
    if user is None:
        user = ""
    else:
        user = user.decode("utf-8")
    return render_template("index.html", user=user)


@app.route("/u/<user_id>")
def print_user(user_id):
    user = get_user(user_id)
    return render_template("user.html", user=user)


@app.route("/create_user", methods=["GET"])
def create_new_user():
    user = create_user()
    return render_template("user.html", user=user)


@app.route("/c/<community_id>")
def print_community(community_id):
    return community_id


@app.route("/p/<post_id>")
def print_post(post_id):
    #post = get_post(post_id)
    #return render_template("post.html", post=post)
    pass


@app.route("/login", methods=["GET", "POST"])
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
