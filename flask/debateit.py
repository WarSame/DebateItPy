from app import create_app, db
from app.models import User, Debate, Post, Community


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Debate': Debate,
        'Post': Post,
        'Community': Community
    }


if __name__ == "__main__":
    app.run()
