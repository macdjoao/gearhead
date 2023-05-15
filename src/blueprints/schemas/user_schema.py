from src.ext.serializer import ma
from src.blueprints.models.user_model import UserModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
