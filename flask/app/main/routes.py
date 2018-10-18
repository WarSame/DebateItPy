from flask import render_template, redirect, request, session, current_app, jsonify, abort
from app.models import User, Community, Post, Debate
from app.main.forms import CreateCommunityForm, CreateDebateForm
from app.auth.oauth import receive_google_token
from app import redis
from app.main import bp


@bp.route("/u", methods=["POST"])
@bp.route("/u/<user_id>", methods=["GET"])
def user(user_id=None):
    if request.method == "POST":
        user = User.create(**request.get_json)
        return 200
    user = User.retrieve_one(id=user_id)
    current_app.logger.info(user)
    if user is None:
        return abort(404)
    return user


@bp.route("/c", methods=["POST"])
@bp.route("/c/<community_id>", methods=["GET"])
def community(community_id=None):
    json = request.get_json()
    current_app.logger.info(json)
    if request.method == "POST":
        Community.create(name=json["name"], description=json["description"])
        return jsonify(success=True)
    community = Community.retrieve_one(id=community_id)
    current_app.logger.info(community)
    if community is None:
        return abort(404)
    response = jsonify(community)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@bp.route("/d/", methods=["POST"])
@bp.route("/d/<debate_id>", methods=["GET"])
def debate(debate_id=None):
    if request.method == "POST":
        Debate.create(**request.get_json)
        return 200
    debate=Debate.retrieve_one(id=debate_id)
    current_app.logger.info(debate)
    if debate is None:
        return abort(404)
    return debate


@bp.route("/p", methods=["POST"])
@bp.route("/p/<post_id>", methods=["GET"])
def post(post_id=None):
    if request.method == "POST":
        post = Post.create(**request.get_json)
        return 200
    post = Post.retrieve_one(id=post_id)
    current_app.logger.info(post)
    if post is None:
        return abort(404)
    return post


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
        debate["id"] = d.id
        debate["description"] = d.description
        top_debates_json.append(debate)
    return jsonify(top_debates_json)
