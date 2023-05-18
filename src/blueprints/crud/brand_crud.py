from src.blueprints.models.brand_model import BrandModel
from src.ext.database import db
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

    def read_brand(self, id: int):
        try:
            brand = BrandModel.query.get(id)
            if brand is None:
                return 'Brand not found', 404
            schema = BrandSchema()
            return f'Brand: {schema.dump(brand)}'
        except Exception as exc:
            print(f'BrandCRUD[READ_BRAND] Error: {exc}')
            return f'Read Error.'
