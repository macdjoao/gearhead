# gearhead

- Criar repositório no github
- Clonar na maquina
- Atualizar gitignore
- Adicionar poetry
- Ativar poetry shell
- Adicionar Flask
- Adicionar Dynaconf
- Configurar Dynaconf em settings.toml (na raiz do projeto)

``
[default]
SQLALCHEMY_DATABASE_URI = 'sqlite:///your.db'
SECRET_KEY = 'your_secret_key'
``

- Adicionar Flask-SQLAlchemy
- Adicionar Flask-Migrate

``
flask db init
flask db migrate
flask db upgrade
``

- Adicionar Flask-Admin (5000/admin)
