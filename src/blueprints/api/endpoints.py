from src.blueprints.api.user_routes import user
from src.blueprints.api.login_route import login
from src.blueprints.api.brand_routes import brand


def init_app(app):
    app.register_blueprint(user)
    app.register_blueprint(login)
    app.register_blueprint(brand)
