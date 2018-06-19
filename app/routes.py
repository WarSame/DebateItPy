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


@app.route("/c/<community_id>")
def display_community(community_id):
    community = get_community(community_id)
    return render_template("community.html", community=community)


@app.route("/c", methods=["POST"])
def create_new_community():
    community = create_community()
    return render_template("community.html", community=community)


@app.route("/p/<post_id>")
def display_post(post_id):
    post = get_post(post_id)
    return render_template("post.html", post=post)

@app.route("/p", methods=["POST"])
def create_new_post():
    post = create_post()
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
