from flask import Flask
from src.ext import configuration
from src.ext import database
from src.ext import migration
from src.ext import admin
from src.ext import serializer
from src.blueprints.endpoints import api


def create_app():

    app = Flask(__name__)
    configuration.init_app(app)
    database.init_app(app)
    serializer.init_app(app)
    migration.init_app(app)
    admin.init_app(app)
    api.init_app(app)

    return app
