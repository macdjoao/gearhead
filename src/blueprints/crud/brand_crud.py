from src.blueprints.models.brand_model import BrandModel
from src.ext.database import db
from werkzeug.security import generate_password_hash
from src.blueprints.schemas.brand_schema import BrandSchema


class BrandCRUD:

    def create_brand(self, payload: dict):
        try:
            name = payload['name'].capitalize()
            code = payload['first_name'].upper()
            brand = BrandModel(name=name, code=code)
            db.session.add(brand)
            db.session.commit()
            schema = BrandSchema()
            return f'Brand successfully created: {schema.dump(brand)}'
        except Exception as exc:
            print(f'BrandCRUD[CREATE_BRAND] Error: {exc}')
            return f'Create Error.'
