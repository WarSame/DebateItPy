from app import ma
from app.models import Community, User, Debate, Post

class CommunitySchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'description')
        model = Community

class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'email')
        model = User

class DebateSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'title', 'text', 'description', 'creator_id', 'community_id', 'posts')
        model = Debate

class PostSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'title', 'text', 'user_id', 'debate_id')
        model = Post
