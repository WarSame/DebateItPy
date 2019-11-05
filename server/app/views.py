from . import ma
from .models import Community, User, Debate, Post
from flask_marshmallow import Marshmallow
from marshmallow import fields


class CommunitySchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Community


class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'email')
        model = User


class PostSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'title', 'text', 'user_id', 'debate_id')
        model = Post


class DebateSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'title', 'description', 'creator_id', 'community_id', 'posts')
        model = Debate
    posts = fields.Nested(PostSchema, many=True)
