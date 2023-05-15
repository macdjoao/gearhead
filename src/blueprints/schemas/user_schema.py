from src.ext.serializer import ma
from src.blueprints.models.user_model import UserModel


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = UserModel
