from app import app
from flask import render_template, redirect
from .forms import EmailPasswordForm, MyForm
import redis

db = redis.Redis(host="redis", port=6379)
db.set("count", 0)


@app.route("/")
def index():
    app.logger.info(db.get("user"))
    db.incr("count", 1)
    count = db.get("count")
    user = db.get("user")
    return render_template("index.html", count=int(count), user=user)


@app.route("/u/<username>")
def print_user(username):
    return username


@app.route("/c/<community_name>")
def print_community(community_name):
    return community_name


@app.route("/submit", methods=("GET", "POST"))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", form=form)


@app.route("/login", methods=("GET", "POST"))
def login():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        app.logger.info(form.email.data)
        app.logger.info("validated")
        return redirect("/")
    app.logger.info("not validated")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    db.delete("user")
    return "logout"
