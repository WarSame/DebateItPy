from .app import create_app, db
from .app.models import User, Debate, Argument, Community
from .app.views import UserSchema, DebateSchema, ArgumentSchema, CommunitySchema


debateit = create_app()


@debateit.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Debate': Debate,
        'Argument': Argument,
        'Community': Community,
        'UserSchema': UserSchema,
        'DebateSchema': DebateSchema,
        'ArgumentSchema': ArgumentSchema,
        'CommunitySchema': CommunitySchema
    }


if __name__ == "__main__":
    debateit.run()
