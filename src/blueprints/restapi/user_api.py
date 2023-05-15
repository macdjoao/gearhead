from flask_restful import Resource
from flask import request
from src.blueprints.schemas.user_schema import UserSchema
from src.blueprints.crud.user_crud import UserCRUD

schema = UserSchema()
crud = UserCRUD()


class UserResource(Resource):

    def post(self):
        try:
            user = schema.load(request.json)
            return crud.create_user(user)
        except Exception as exc:
            return f'UserResource[POST] Error: {exc}'

    def get(self):
        try:
            return crud.read_users()
        except Exception as exc:
            return f'UserResource[GET] Error: {exc}'


class UserResourceList(Resource):

    def get(self, id):
        try:
            return crud.read_user(id)
        except Exception as exc:
            return f'UserResourceList[GET] Error: {exc}'

    def delete(self, id):
        try:
            return crud.delete_user(id)
        except Exception as exc:
            return f'UserResourceList[DELETE] Error: {exc}'
