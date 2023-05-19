from flask import Blueprint
from flask import request
from src.blueprints.schemas.brand_schema import BrandSchema
from src.blueprints.crud.brand_crud import BrandCRUD
from flask_jwt_extended import jwt_required

schema = BrandSchema()
crud = BrandCRUD()

brand = Blueprint('brand', __name__, url_prefix='/api/v1')


@brand.route('/brand', methods=['POST'])
# @jwt_required()
def post_brand():
    try:
        brand = schema.load(request.json)
        return crud.create_brand(brand)
    except Exception as exc:
        print(f'[post_brand] Error: {exc}')
        return 'Create error.'


@brand.route('/brand/<int:id>', methods=['GET'])
# @jwt_required()
def get_brand(id: int):
    try:
        return crud.read_brand(id)
    except Exception as exc:
        print(f'[get_brand] Error: {exc}')
        return 'Read error.'


@brand.route('/brand', methods=['GET'])
# @jwt_required()
def get_brands():
    try:
        return crud.read_brands()
    except Exception as exc:
        print(f'[get_brands] Error: {exc}')
        return 'Read error.'


@brand.route('/brand/<int:id>', methods=['PATCH'])
# @jwt_required()
def patch_brand(id: int):
    try:
        payload = request.json
        return crud.update_brand(id, payload)
    except Exception as exc:
        print(f'[patch_brand] Error: {exc}')
        return 'Update error.'


@brand.route('/brand/<int:id>', methods=['DELETE'])
# @jwt_required()
def delete_brand(id: int):
    try:
        return crud.delete_brand(id)
    except Exception as exc:
        print(f'[delete_brand] Error: {exc}')
        return 'Delete error.'
