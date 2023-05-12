from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.ext.database import db
from ..models import User, Brand, Vehicle, Part

admin = Admin(name='Gearhead', template_mode='bootstrap3')


def init_app(app):
    admin.init_app(app)
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Brand, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(ModelView(Part, db.session))
