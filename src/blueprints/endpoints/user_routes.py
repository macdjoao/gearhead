from flask import Blueprint
from flask import request
from src.blueprints.schemas.user_schema import UserSchema
from src.blueprints.crud.user_crud import UserCRUD

schema = UserSchema()
crud = UserCRUD()

user = Blueprint('user', __name__, url_prefix='/api/v1/user')


@user.route('/create', methods=['POST'])
def post_user():
    try:
        user = schema.load(request.json)
        return crud.create_user(user)
    except Exception as exc:
        print(f'[post_user] Error: {exc}')
        return 'Create error.'


@user.route('/read/<int:id>')
def get_user(id: int):
    try:
        return crud.read_user(id)
    except Exception as exc:
        print(f'[get_user] Error: {exc}')
        return 'Read error.'


@user.route('/read')
def get_users():
    try:
        return crud.read_users()
    except Exception as exc:
        print(f'[get_users] Error: {exc}')
        return 'Read error.'


@user.route('/update/<int:id>', methods=['PATCH'])
def patch_user(id: int):
    try:
        payload = request.json
        return crud.update_user(id, payload)
    except Exception as exc:
        print(f'[patch_user] Error: {exc}')
        return 'Update error.'


@user.route('/delete/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    try:
        return crud.delete_user(id)
    except Exception as exc:
        print(f'[delete_user] Error: {exc}')
        return 'Delete error.'
