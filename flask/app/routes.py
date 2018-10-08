from app import app
from flask import render_template, redirect, request, session
import redis
from .models import User, Community, Post, Debate
from .forms import CreateCommunityForm, CreateDebateForm
from .oauth import receive_google_token
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify
redis = redis.Redis(host="redis", port=6379)

db = SQLAlchemy(app)
cors = CORS(app)


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
    return redirect("index.html")


@app.route("/test")
def test():
    response = jsonify({"key": "value"})
    return response


@app.route("/u", methods=["POST"])
@app.route("/u/<user_id>", methods=["GET"])
def user(user_id=None):
    if request.method == "POST":
        user_dict = dict()
        user_dict["name"] = request.form["name"]
        user_dict["email"] = request.form["email"]
        user = User.create(**user_dict)
    else:
        user = User.retrieve_one(id=user_id)
    app.logger.info(user)
    if user is None:
        return render_template("missing.html")
    return render_template("user.html", user=user)


@app.route("/c/create", methods=["GET", "POST"])
def create_community():
    app.logger.info("Creating community")
    form = CreateCommunityForm()
    if form.validate_on_submit():
        app.logger.info("Community form validated")
        community_dict = dict()
        community_dict["name"] = form.name.data
        community_dict["description"] = form.description.data
        community = Community.create(**community_dict)
        app.logger.info("Created community, displaying")
        return render_template("community.html", community=community)
    return render_template("create_community.html", form=form)


@app.route("/c/<community_id>", methods=["GET"])
def community(community_id=None):
    community = Community.retrieve_one(id=community_id)
    if community is None:
        return render_template("missing.html")
    return render_template("community.html", community=community)


@app.route("/d/create", methods=["GET", "POST"])
def create_debate():
    app.logger.info("Creating debate")
    form = CreateDebateForm()
    if form.validate_on_submit():
        app.logger.info("Debate form validated")
        debate_dict = dict([(
            "title", form.title.data),
            ("text", form.text.data),
            ("creator_id", session["user_id"]),
            ("community_id", form.community_id.data)
        ])
        debate = Debate.create(**debate_dict)
        app.logger.info("Created debate, displaying")
        return redirect("/d/{}".format(debate.id))
    return render_template("create_debate.html", form=form)


@app.route("/d/<debate_id>", methods=["GET"])
def debate(debate_id=None):
    debate = Debate.retrieve_one(id=debate_id)
    if debate is None:
        return render_template("missing.html")
    return render_template("debate.html", debate=debate)


@app.route("/p", methods=["POST"])
@app.route("/p/<post_id>", methods=["GET"])
def post(post_id=None):
    if request.method == "POST":
        post_dict = dict()
        post_dict["title"] = request.form["title"]
        post_dict["text"] = request.form["text"]
        post_dict["user_id"] = request.form["user_id"]
        post = Post.create(**post_dict)
    else:
        post = Post.retrieve_one(id=post_id)
    if post is None:
        return render_template("missing.html")
    return render_template("post.html", post=post)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        user = User.create(name=name)
        return redirect("/u/{}".format(user.id))
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("user_name", None)
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
    session["user_id"] = user.id
    session["user_name"] = user.name
    app.logger.info("User id in session: {}".format(user_id))
    app.logger.info("User name in session: {}".format(user_name))
    return user_name
