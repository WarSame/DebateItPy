from app import app
from flask import render_template, redirect, request
import redis
from .models import User, Community, Post
from .oauth import receive_google_token
from flask_sqlalchemy import SQLAlchemy

redis = redis.Redis(host="redis", port=6379)


db = SQLAlchemy(app)


def initialize_db():
    db.init_app(app)
    with app.app_context():
        db.metadata.drop_all(bind=db.engine)
        db.metadata.create_all(bind=db.engine)
        db.session.commit()


@app.before_first_request
def setup():
    initialize_db()


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
        user = User.create(name=name)
    else:
        user = User.retrieve(row_id=user_id)
    app.logger.info(user)
    if user is None:
        return render_template("missing.html")
    return render_template("user.html", user=user)


@app.route("/c/", methods=["POST"])
@app.route("/c/<community_id>", methods=["GET"])
def display_community(community_id=None):
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        community = Community.create(name=name, description=description)
    else:
        community = Community.retrieve(row_id=community_id)
    if community is None:
        return render_template("missing.html")
    return render_template("community.html", community=community)


@app.route("/p", methods=["POST"])
@app.route("/p/<post_id>", methods=["GET"])
def display_post(post_id):
    if request.method == "POST":
        title = request.form["title"]
        text = request.form["text"]
        user_id = request.form["user_id"]
        post = Post.create(title=title, text=text, user_id=user_id)
    else:
        post = Post.retrieve(row_id=post_id)
    if post is None:
        return render_template("missing.html")
    return render_template("post.html", post=post)


@app.route("/login", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        user = User.create(name=name)
        return render_template("user.html", user=user)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    redis.delete("user")
    return redirect("/")


@app.route("/google/token_signin", methods=["POST"])
def token_signin():
    token = request.form["token"]
    user_from_google = receive_google_token(token)
    user_id = user_from_google["user_id"]
    user_name = user_from_google["user_name"]
    user_email = user_from_google["user_email"]
    user = User.retrieve_one(google_id=user_id)
    if user:
        app.logger.info("Found user by google id {}".format(user))
    else:
        app.logger.info("Didn't find user by google id")
        user = User.create(name=user_name, google_id=user_id, email=user_email)
    app.logger.info(user_id)
    return render_template("user.html", user=user)
