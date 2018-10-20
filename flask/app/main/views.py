from app import ma
from app.models import Community, User

class CommunitySchema(ma.ModelSchema):
    class Meta:
        model = Community

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User