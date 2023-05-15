from flask_marshmallow import Marshmallow


def init_app(app):
    Marshmallow(app)
