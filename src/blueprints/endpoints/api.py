from src.blueprints.endpoints.user_routes import user


def init_app(app):
    app.register_blueprint(user)
