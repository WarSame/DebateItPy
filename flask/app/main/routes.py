from flask import render_template, redirect, request, session, current_app
from app.models import User, Community, Post, Debate
from app.main.forms import CreateCommunityForm, CreateDebateForm
from app.auth.oauth import receive_google_token
from flask import jsonify
from app import cors, redis
from app.main import bp


@bp.route("/")
def index():
    return redirect("index.html")


@bp.route("/u", methods=["POST"])
@bp.route("/u/<user_id>", methods=["GET"])
def user(user_id=None):
    if request.method == "POST":
        user_dict = dict()
        user_dict["name"] = request.form["name"]
        user_dict["email"] = request.form["email"]
        user = User.create(**user_dict)
    else:
        user = User.retrieve_one(id=user_id)
    current_app.logger.info(user)
    if user is None:
        return render_template("missing.html")
    return render_template("user.html", user=user)


@bp.route("/c/create", methods=["GET", "POST"])
def create_community():
    current_app.logger.info("Creating community")
    form = CreateCommunityForm()
    if form.validate_on_submit():
        current_app.logger.info("Community form validated")
        community_dict = dict()
        community_dict["name"] = form.name.data
        community_dict["description"] = form.description.data
        community = Community.create(**community_dict)
        current_app.logger.info("Created community, displaying")
        return render_template("community.html", community=community)
    return render_template("create_community.html", form=form)


@bp.route("/c/<community_id>", methods=["GET"])
def community(community_id=None):
    community = Community.retrieve_one(id=community_id)
    if community is None:
        return render_template("missing.html")
    return render_template("community.html", community=community)


@bp.route("/d/create", methods=["GET", "POST"])
def create_debate():
    current_app.logger.info("Creating debate")
    form = CreateDebateForm()
    if form.validate_on_submit():
        current_app.logger.info("Debate form validated")
        debate_dict = dict([(
            "title", form.title.data),
            ("text", form.text.data),
            ("creator_id", session["user_id"]),
            ("community_id", form.community_id.data)
        ])
        debate = Debate.create(**debate_dict)
        current_app.logger.info("Created debate, displaying")
        return redirect("/d/{}".format(debate.id))
    return render_template("create_debate.html", form=form)


@bp.route("/d/<debate_id>", methods=["GET"])
def debate(debate_id=None):
    debate = Debate.retrieve_one(id=debate_id)
    if debate is None:
        return render_template("missing.html")
    return render_template("debate.html", debate=debate)


@bp.route("/top/d/<count>", methods=["GET"])
def top_debates(count=0):
    current_app.logger.info("Retrieving top " + count + " rows")
    top_debates = Debate.retrieve_some(count)
    current_app.logger.info("Retrieved {} rows".format(len(top_debates)))
    top_debates_json = []
    for d in top_debates:
        debate = dict()
        debate["title"] = d.title
        debate["text"] = d.text
        top_debates_json.append(debate)
    return jsonify(top_debates_json)


@bp.route("/p", methods=["POST"])
@bp.route("/p/<post_id>", methods=["GET"])
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


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        user = User.create(name=name)
        return redirect("/u/{}".format(user.id))
    else:
        return render_template("login.html")


@bp.route("/logout")
def logout():
    session.pop("user_id", None)
    session.pop("user_name", None)
    return redirect("/")


@bp.route("/google/token_signin", methods=["POST"])
def token_signin():
    json = request.get_json()
    if not json:
        return jsonify(
            {"message": "Empty request json"}), 400
    current_app.logger.info("Request is {}".format(json))
    token = json["token"]
    if token is None:
        return jsonify({"error": "Missing token"}), 400
    current_app.logger.info("Token is {}".format(token))
    user_from_google = receive_google_token(token)
    if user_from_google is None:
        return jsonify({"error": "Google user matching ID not found"}), 404
    user_id = user_from_google["user_id"]
    user_name = user_from_google["user_name"]
    user_email = user_from_google["user_email"]
    user = User.retrieve_one(google_id=user_id)
    if user:
        current_app.logger.info("Found user by google id {}".format(user))
    else:
        current_app.logger.info("Didn't find user by google id")
        user = User.create(name=user_name, google_id=user_id, email=user_email)
    return jsonify(user)