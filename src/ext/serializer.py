from flask_marshmallow import Marshmallow
from src.ext.database import db


def init_app(app):
    Marshmallow(app)
