from flask_restful import Resource
from flask import request
from src.blueprints.schemas.user_schema import UserSchema
from src.blueprints.crud.user_crud import UserCRUD

schema = UserSchema()
crud = UserCRUD()


class UserResource(Resource):

    def post(self):
        user = schema.load(request.json)
        return crud.create_user(user)

    def get(self):
        return 'get user'

    def patch(self):
        return 'patch user'

    def delete(self):
        return 'delete user'


class UserListResource(Resource):

    def get(self):
        return 'get list user'
