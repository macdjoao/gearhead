# gearhead

- Criar repositorio no github
- Clonar na maquina
- Atualizar gitignore
- Adicionar poetry
- Ativar poetry shell
- Adicionar Flask
- Adicionar Dynaconf
- Configurar Dynaconf em settings.toml (na raiz)
``sh
[default]
SQLALCHEMY_DATABASE_URI = 'sqlite:///your.db'
SECRET_KEY = 'your_secret_key'
``
- Adicionar Flask-SQLAlchemy
- Adicionar Flask-Migrate
- Instanciar alchemy e migrate em app.py
- flask db init; flask db migrate; flask db upgrade
- Adicionado Flask-Admin (5000/admin)
- Adicionar .env {FLASK_APP=src/app.py}
