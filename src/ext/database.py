from flask_sqlalchemy import SQLAlchemy

# Diferente dos outros factories, 'db' foi atribuído a uma variável, pois essa variável será necessária em outras partes do código.
db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
