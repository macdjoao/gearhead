from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src.ext.database import db
from src.blueprints.models.user_model import UserModel
from src.blueprints.models.brand_model import BrandModel
from src.blueprints.models.vehicle_model import VehicleModel
from src.blueprints.models.part_model import PartModel

admin = Admin(name='Gearhead', template_mode='bootstrap3')


def init_app(app):
    admin.init_app(app)
    admin.add_view(ModelView(UserModel, db.session))
    admin.add_view(ModelView(BrandModel, db.session))
    admin.add_view(ModelView(VehicleModel, db.session))
    admin.add_view(ModelView(PartModel, db.session))
