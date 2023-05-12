from flask_migrate import Migrate
from src.ext.database import db


def init_app(app):
    Migrate(app, db)
