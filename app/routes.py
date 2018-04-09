from app import app, docker


@app.route("/")
def thisfunc():
    return docker.info()

