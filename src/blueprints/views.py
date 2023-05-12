def init_app(app):
    @app.route('/')
    def index():
        return 'Olá'
