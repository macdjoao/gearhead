from src.blueprints.endpoints.user_routes import user
from src.blueprints.endpoints.login_route import login


def init_app(app):
    app.register_blueprint(user)
    app.register_blueprint(login)
