from flask import Blueprint
from flask_restful import Api
from .user_api import UserResource

bp = Blueprint("restapi", __name__, url_prefix="/api/")
api = Api(bp)
api.add_resource(UserResource, "/user/")


def init_app(app):
    app.register_blueprint(bp)
