from flask import render_template, redirect, request, session, current_app, jsonify, abort
from app.models import User, Community, Post, Debate
from app.main.forms import CreateCommunityForm, CreateDebateForm
from app.auth.oauth import receive_google_token
from app import redis
from app.main import bp
from app.main.views import CommunitySchema, UserSchema


@bp.route("/api/u/", methods=["POST"])
def create_user(user_id=None):
    if request.method == "POST":
        user = User.create(**request.get_json)
        return 200
    user = User.retrieve_one(id=user_id)
    current_app.logger.info(user)
    if user is None:
        return abort(404)
    return user


@bp.route("/api/u/<user_id>", methods=["GET"])
def get_user(user_id=None):
    if request.method == "POST":
        user = User.create(**request.get_json)
        return 200
    user = User.retrieve_one(id=user_id)
    current_app.logger.info(user)
    if user is None:
        return abort(404)
    return user


@bp.route("/api/c/<community_id>", methods=["GET"])
def get_specific_community(community_id=None):
    community = Community.retrieve_one(id=community_id)
    current_app.logger.info(community)
    if community is None:
        return abort(404)
    community_schema = CommunitySchema()
    community_json = community_schema.dump(community).data
    current_app.logger.info(community_json)
    return jsonify(community_json)


@bp.route("/api/c", methods=["GET"])
def get_all_communities():
    return None


@bp.route("/api/c", methods=["POST"])
def create_community():
    json = request.get_json()
    current_app.logger.info(json)
    name = json["name"]
    if Community.retrieve_one(name=name) is not None:
        return jsonify(success=False, reason='Community already exists')
    Community.create(name=name, description=json["description"])
    return jsonify(success=True)


@bp.route("/api/d/", methods=["POST"])
@bp.route("/api/d/<debate_id>", methods=["GET"])
def debate(debate_id=None):
    if request.method == "POST":
        Debate.create(**request.get_json)
        return 200
    debate=Debate.retrieve_one(id=debate_id)
    current_app.logger.info(debate)
    if debate is None:
        return abort(404)
    return debate


@bp.route("/api/p/", methods=["POST"])
@bp.route("/api/p/<post_id>", methods=["GET"])
def post(post_id=None):
    if request.method == "POST":
        post = Post.create(**request.get_json)
        return 200
    post = Post.retrieve_one(id=post_id)
    current_app.logger.info(post)
    if post is None:
        return abort(404)
    return post


@bp.route("/api/top/d/<count>", methods=["GET"])
def top_debates(count=0):
    current_app.logger.info("Retrieving top " + count + " rows")
    top_debates = Debate.retrieve_some(count)
    current_app.logger.info("Retrieved {} rows".format(len(top_debates)))
    top_debates_json = []
    for d in top_debates:
        debate = dict()
        debate["title"] = d.title
        debate["text"] = d.text
        debate["id"] = d.id
        debate["description"] = d.description
        top_debates_json.append(debate)
    return jsonify(top_debates_json)
