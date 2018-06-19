from app import app
from flask import render_template, redirect, request
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


@app.route("/u/", methods=["POST"])
@app.route("/u/<user_id>", methods=["GET"])
def display_user(name=None, user_id=None):
    if request.method == "POST":
        user = create_user(name=name)
    else:
        user = get_user(user_id)
    return render_template("user.html", user=user)


@app.route("/c/", methods=["POST"])
@app.route("/c/<community_id>", methods=["GET"])
def display_community(name=None, community_id=None):
    if request.method == "POST":
        community = create_community()
    else:
        community = get_community(community_id)
    return render_template("community.html", community=community)


@app.route("/p", methods=["POST"])
@app.route("/p/<post_id>", methods=["GET"])
def display_post(post_id):
    if request.method == "POST":
        post = create_post()
    else:
        post = get_post(post_id)
    return render_template("post.html", post=post)


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
