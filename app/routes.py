from app import app
from flask import render_template, session


@app.route("/")
def index():
    return "hi"
    #session['key'] = 'value'
    #return render_template("index.html")


@app.route("/u/<username>")
def print_user(username):
    return username


@app.route("/c/<community_name>")
def print_community(community_name):
    return community_name


@app.route("/login")
def login():
    return session.get('key', 'not set')#return render_template("login.html")
