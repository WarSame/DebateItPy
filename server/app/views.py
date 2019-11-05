from . import ma
from .models import Community, User, Debate, Argument
from marshmallow import fields


class CommunitySchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Community


class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'email')
        model = User


class ArgumentSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'title', 'content', 'user_id', 'debate_id')
        model = Argument


class DebateSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'title', 'description', 'creator_id', 'community_id', 'posts')
        model = Debate
    posts = fields.Nested(ArgumentSchema, many=True)
