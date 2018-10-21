from app import ma
from app.models import Community, User, Debate, Post

class CommunitySchema(ma.ModelSchema):
    class Meta:
        fields = ('name', 'description', 'id')
        model = Community

class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('name', 'id')
        model = User

class DebateSchema(ma.ModelSchema):
    class Meta:
        fields = ('title', 'text', 'description', 'creator_id', 'community_id')
        model = Debate

class PostSchema(ma.ModelSchema):
    class Meta:
        fields = ('title', 'text', 'user_id', 'debate_id')
        model = Post
