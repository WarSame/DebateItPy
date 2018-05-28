from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/u/<username>")
def print_user(username):
    return username


@app.route("/c/<community_name>")
def print_community(community_name):
    return community_name

