from .. import models
from flask import json


def retrieve_community(app, ids):
    return app.get('/api/c/{}'.format(ids["community_id"]), follow_redirects=True)


def retrieve_user(app, ids):
    return app.get('/api/u/{}'.format(ids["user_id"]), follow_redirects=True)


def retrieve_debate(app, ids):
    return app.get('/api/d/{}'.format(ids["debate_id"]), follow_redirects=True)


def retrieve_arguments(app, ids):
    return app.get('/api/d/{}/a/'.format(ids["debate_id"]), follow_redirects=True)


def insert_user(app):
    u = {
        "name": "graeme",
        "email": "graeme@test.com",
        "google_id": "something"
    }
    post_response = app.post(
        '/api/u/',
        data=json.dumps(u),
        content_type="application/json"
    )
    return post_response


def insert_community(app):
    c = {
        "name": "mycommunity",
        "description": "something"
    }
    post_response = app.post(
        '/api/c/',
        data=json.dumps(c),
        content_type="application/json"
    )
    return post_response


def insert_debate(app, u_id, c_id):
    d = {
        "title": "somedebate",
        "description": "somedescription",
        "creator_id": u_id,
        "community_id": c_id
    }
    post_response = app.post(
        '/api/d/',
        data=json.dumps(d),
        content_type="application/json"
    )
    return post_response


def insert_arguments(app, u_id, d_id):
    arg1 = {
        "title": "sometitle",
        "content": "somecontent",
        "user_id": u_id,
        "debate_id": d_id
    }
    arg2 = {
        "title": "sometitle",
        "content": "somecontent",
        "user_id": u_id,
        "debate_id": d_id
    }
    post_response_1 = app.post(
        '/api/a/',
        data=json.dumps(arg1),
        content_type="application/json"
    )
    post_response_2 = app.post(
        '/api/a/',
        data=json.dumps(arg2),
        content_type="application/json"
    )
    return [post_response_1, post_response_2]


def fill_db_api(app):
    ids = dict()
    ids["user_id"] = insert_user(app=app).json["id"]
    ids["community_id"] = insert_community(app=app).json["id"]
    ids["debate_id"] = insert_debate(app=app, c_id=ids["community_id"], u_id=ids["user_id"]).json["id"]
    ids["arg_ids"] = list(
        map(
            lambda x: x.json["id"],
            insert_arguments(app=app, d_id=ids["debate_id"], u_id=ids["user_id"])
        )
    )
    return ids
