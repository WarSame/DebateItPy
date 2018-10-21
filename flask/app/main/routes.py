from flask import render_template, redirect, request, session, current_app, jsonify, abort
from app.models import User, Community, Post, Debate
from app.main.forms import CreateCommunityForm, CreateDebateForm
from app.auth.oauth import receive_google_token
from app import redis
from app.main import bp
from app.views import CommunitySchema, UserSchema, DebateSchema, PostSchema


@bp.route("/api/u/", methods=["POST"])
def create_user(user_id=None):
    json = request.get_json()
    current_app.logger.info(json)
    if User.retrieve_one(name=json["name"]) is not None:
        return jsonify(success=False, reason='User with that name already exists')
    user = User.create(**json)
    user_json = UserSchema().dump(user).data
    return jsonify(user_json)


@bp.route("/api/u/<user_id>", methods=["GET"])
def get_user(user_id=None):
    user = User.retrieve_one(id=user_id)
    current_app.logger.info(user)
    if user is None:
        return abort(404)
    user_json = UserSchema().dump(user).data
    current_app.logger.info(user_json)
    return jsonify(user_json)


@bp.route("/api/c/<community_id>", methods=["GET"])
def get_specific_community(community_id=None):
    community = Community.retrieve_one(id=community_id)
    current_app.logger.info(community)
    if community is None:
        return abort(404)
    community_json = CommunitySchema().dump(community).data
    current_app.logger.info(community_json)
    return jsonify(community_json)


@bp.route("/api/c/", methods=["POST"])
def create_community():
    json = request.get_json()
    current_app.logger.info(json)
    if Community.retrieve_one(name=json["name"]) is not None:
        return jsonify(success=False, reason='Community with that name already exists')
    community = Community.create(**json)
    community_json = CommunitySchema().dump(community).data
    return jsonify(community_json)


@bp.route("/api/d/<debate_id>", methods=["GET"])
def get_debate(debate_id=None):
    debate = Debate.retrieve_one(id=debate_id)
    current_app.logger.info(debate)
    if debate is None:
        return abort(404)
    debate_json = DebateSchema().dump(debate).data
    current_app.logger.info(debate_json)
    return jsonify(debate_json)


@bp.route("/api/d/", methods=["POST"])
def create_debate():
    json = request.get_json()
    current_app.logger.info(json)
    debate = Debate.create(**json)
    debate_json = DebateSchema().dump(debate).data
    return jsonify(debate_json)


@bp.route("/api/p/<post_id>", methods=["GET"])
def get_post(post_id=None):
    post = Post.retrieve_one(id=post_id)
    current_app.logger.info(post)
    if post is None:
        return abort(404)
    post_json = PostSchema().dump(post).data
    current_app.logger.info(post_json)
    return jsonify(post_json)


@bp.route("/api/p/", methods=["POST"])
def create_post():
    json = request.get_json()
    current_app.logger.info(json)
    post = Post.create(**json)
    post_json = PostSchema().dump(post).data
    return jsonify(post_json)


@bp.route("/api/top/d/<count>", methods=["GET"])
def top_debates(count=0):
    current_app.logger.info("Retrieving top " + count + " rows")
    top_debates = Debate.retrieve_some(count)
    current_app.logger.info("Retrieved {} rows".format(len(top_debates)))
    top_debates_json = UserSchema(many=True).dump(top_debates).data
    return jsonify(top_debates_json)
