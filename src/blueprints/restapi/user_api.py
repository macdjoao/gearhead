from flask_restful import Resource


class UserResource(Resource):

    def post(self):
        return 'post user'

    def get(self):
        return 'get user'

    def patch(self):
        return 'patch user'

    def delete(self):
        return 'delete user'


class UserListResource(Resource):

    def get(self):
        return 'get list user'
