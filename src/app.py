from flask import Flask
from src.ext import configuration
from src.ext import database
from src.ext import migration
from src.ext import admin

app = Flask(__name__)
configuration.init_app(app)
database.init_app(app)
migration.init_app(app)
admin.init_app(app)


@app.route('/')
def index():
    return 'Olá'
