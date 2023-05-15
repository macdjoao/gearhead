from flask_marshmallow import Marshmallow

# Diferente dos outros factories, 'ma' foi atribuído a uma variável, pois essa variável será necessária em outras partes do código.
ma = Marshmallow()


def init_app(app):
    ma.init_app(app)
