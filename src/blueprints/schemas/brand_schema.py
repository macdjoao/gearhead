from src.ext.serializer import ma
from src.blueprints.models.brand_model import BrandModel


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BrandModel
