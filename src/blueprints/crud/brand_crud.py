from src.blueprints.models.brand_model import BrandModel
from src.ext.database import db
from src.blueprints.schemas.brand_schema import BrandSchema


class BrandCRUD:

    def create_brand(self, payload: dict):
        schema = BrandSchema()
        try:
            name = payload['name'].capitalize()
            code = payload['code'].upper()
            brand = BrandModel(name=name, code=code)
            db.session.add(brand)
            db.session.commit()
            return f'Brand successfully created: {schema.dump(brand)}'
        except Exception as exc:
            print(f'BrandCRUD[CREATE_BRAND] Error: {exc}')
            return f'Create Error.'

    def read_brand(self, id: int):
        schema = BrandSchema()
        try:
            brand = BrandModel.query.get(id)
            if brand is None:
                return 'Brand not found', 404
            return f'Brand: {schema.dump(brand)}'
        except Exception as exc:
            print(f'BrandCRUD[READ_BRAND] Error: {exc}')
            return f'Read Error.'

    def read_brands(self):
        schema = BrandSchema(many=True)
        try:
            brands = BrandModel.query.all()
            if brands is None:
                return 'Brands not found', 404
            return f'Brand: {schema.dump(brands)}'
        except Exception as exc:
            print(f'BrandCRUD[READ_BRANDS] Error: {exc}')
            return f'Read Error.'

    def update_brand(self, id: int, payload: dict):
        try:
            brand = BrandModel.query.get(id)
            if brand is None:
                return 'Brand not found', 404
            if 'name' in payload:
                brand.name = payload['name'].capitalize()
            if 'code' in payload:
                brand.code = payload['code'].upper()
            db.session.commit()
            return f'Brand successfully updated'
        except Exception as exc:
            print(f'BrandCRUD[UPDATE_BRAND] Error: {exc}')
            return f'Update Error.'

    def delete_brand(self, id: int):
        try:
            brand = BrandModel.query.get(id)
            if brand is None:
                return 'Brand not found', 404
            BrandModel.query.filter_by(id=id).delete()
            db.session.commit()
            return f'Brand successfully deleted.'
        except Exception as exc:
            print(f'BrandCRUD[DELETE_BRAND] Error: {exc}')
            return f'Delete Error.'
