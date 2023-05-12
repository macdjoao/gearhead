from flask import Flask
from dynaconf import FlaskDynaconf
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin

app = Flask(__name__)

FlaskDynaconf(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app, name='microblog', template_mode='bootstrap3')


@app.route('/')
def index():
    return 'Olá'
