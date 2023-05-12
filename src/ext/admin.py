from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.ext.database import db
from src.blueprints.models.user import User as UserModel
from src.blueprints.models.brand import Brand as BrandModel
from src.blueprints.models.vehicle import Vehicle as VehicleModel
from src.blueprints.models.part import Part as PartModel

admin = Admin(name='Gearhead', template_mode='bootstrap3')


def init_app(app):
    admin.init_app(app)
    admin.add_view(ModelView(UserModel, db.session))
    admin.add_view(ModelView(BrandModel, db.session))
    admin.add_view(ModelView(VehicleModel, db.session))
    admin.add_view(ModelView(PartModel, db.session))
