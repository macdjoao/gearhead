from flask import Blueprint
from flask import request
from src.blueprints.schemas.user_schema import UserSchema
from src.blueprints.crud.user_crud import UserCRUD
from flask_jwt_extended import jwt_required

schema = UserSchema()
crud = UserCRUD()

user = Blueprint('user', __name__, url_prefix='/api/v1')


@user.route('/user', methods=['POST'])
@jwt_required()
def post_user():
    try:
        user = schema.load(request.json)
        return crud.create_user(user)
    except Exception as exc:
        print(f'[post_user] Error: {exc}')
        return 'Create error.'


@user.route('/user/<int:id>', methods=['GET'])
@jwt_required()
def get_user(id: int):
    try:
        return crud.read_user(id)
    except Exception as exc:
        print(f'[get_user] Error: {exc}')
        return 'Read error.'


@user.route('/user', methods=['GET'])
@jwt_required()
def get_users():
    try:
        return crud.read_users()
    except Exception as exc:
        print(f'[get_users] Error: {exc}')
        return 'Read error.'


@user.route('/user/<int:id>', methods=['PATCH'])
@jwt_required()
def patch_user(id: int):
    try:
        payload = request.json
        return crud.update_user(id, payload)
    except Exception as exc:
        print(f'[patch_user] Error: {exc}')
        return 'Update error.'


@user.route('/user/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id: int):
    try:
        return crud.delete_user(id)
    except Exception as exc:
        print(f'[delete_user] Error: {exc}')
        return 'Delete error.'
