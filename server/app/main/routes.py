from flask import request, current_app, jsonify, abort
from ..models import User, Community, Argument, Debate
from ..main import bp
from ..views import CommunitySchema, UserSchema, DebateSchema, ArgumentSchema


@bp.route("/api/u/", methods=["POST"])
def create_user(user_id=None):
    json = request.get_json()
    current_app.logger.info(json)
    if User.retrieve_one(name=json["name"]) is not None:
        return jsonify(success=False, reason='User with that name already exists')
    user = User.create(**json)
    user_json = UserSchema().dump(user)
    return jsonify(user_json)


@bp.route("/api/u/<user_id>", methods=["GET"])
def get_user(user_id=None):
    user = User.retrieve_one(id=user_id)
    current_app.logger.info(user)
    if user is None:
        return abort(404)
    user_json = UserSchema().dump(user)
    current_app.logger.info(user_json)
    return jsonify(user_json)


@bp.route("/api/c/<community_id>", methods=["GET"])
def get_specific_community(community_id=None):
    community = Community.retrieve_one(id=community_id)
    current_app.logger.info(community)
    if community is None:
        return abort(404)
    community_json = CommunitySchema().dump(community)
    current_app.logger.info(community_json)
    return jsonify(community_json)


@bp.route("/api/c/", methods=["POST"])
def create_community():
    json = request.get_json()
    current_app.logger.info(json)
    if Community.retrieve_one(name=json["name"]) is not None:
        return jsonify(success=False, reason='Community with that name already exists')
    community = Community.create(**json)
    community_json = CommunitySchema().dump(community)
    return jsonify(community_json)


@bp.route("/api/d/<debate_id>", methods=["GET"])
def get_debate(debate_id=None):
    debate = Debate.retrieve_one(id=debate_id)
    current_app.logger.info(debate)
    if debate is None:
        return abort(404)
    debate_json = DebateSchema().dump(debate)
    current_app.logger.info(debate_json)
    return jsonify(debate_json)


@bp.route("/api/d/", methods=["POST"])
def create_debate():
    json = request.get_json()
    current_app.logger.info(json)
    debate = Debate.create(**json)
    debate_json = DebateSchema().dump(debate)
    return jsonify(debate_json)


@bp.route("/api/a/<argument_id>", methods=["GET"])
def get_argument(argument_id=None):
    argument = Argument.retrieve_one(id=argument_id)
    current_app.logger.info(argument)
    if argument is None:
        return abort(404)
    argument_json = ArgumentSchema().dump(argument)
    current_app.logger.info(argument_json)
    return jsonify(argument_json)


@bp.route("/api/a/", methods=["POST"])
def create_argument():
    json = request.get_json()
    current_app.logger.info(json)
    argument = Argument.create(**json)
    argument_json = ArgumentSchema().dump(argument)
    return jsonify(argument_json)


@bp.route("/api/top/d/<count>", methods=["GET"])
def top_debates(count=0):
    current_app.logger.info("Retrieving top {} rows".format(count))
    top_debates = Debate.retrieve_some(count)
    current_app.logger.info("Retrieved {} rows".format(len(top_debates)))
    top_debates_json = DebateSchema(many=True).dump(top_debates)
    current_app.logger.info("JSON is {}".format(top_debates_json))
    return jsonify(top_debates_json)
