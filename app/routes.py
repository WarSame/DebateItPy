from app import app


@app.route("/")
def thisfunc():
    return "$"

