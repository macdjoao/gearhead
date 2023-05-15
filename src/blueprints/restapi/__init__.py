from flask import Blueprint
from flask_restful import Api
from .user_api import UserResource, UserListResource

bp = Blueprint("restapi", __name__, url_prefix="/api/")
api = Api(bp)
api.add_resource(UserResource, "/user/")
api.add_resource(UserListResource, "/user/all")


def init_app(app):
    app.register_blueprint(bp)
