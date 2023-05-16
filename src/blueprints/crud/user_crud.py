from src.blueprints.models.user_model import UserModel
from src.ext.database import db
from werkzeug.security import generate_password_hash


class UserCRUD:

    def create_user(self, payload):
        try:
            user = UserModel(email=payload['email'], first_name=payload['first_name'],
                             last_name=payload['last_name'], password=payload['password'])
            user.password = generate_password_hash(user.password)
            db.session.add(user)
            db.session.commit()
            return f'User successfully created: {user}'
        except Exception as exc:
            print(f'UserCRUD[CREATE_USER] Error: {exc}')
            return f'Create Error'

    # Corrigir retorno
    def read_user(self, id):
        try:
            query = UserModel.query.filter(UserModel.id == id)
            return f'User: {query}'
        except Exception as exc:
            print(f'UserCRUD[READ_USER] Error: {exc}')
            return f'Read Error'

    # Corrigir retorno
    def read_users(self):
        try:
            query = UserModel.query.all()
            return f'Users: {query}'
        except Exception as exc:
            print(f'UserCRUD[READ_USERS] Error: {exc}')
            return f'Read Error'

    # Implementar
    def update_user(self, id):
        try:
            pass
        except Exception as exc:
            print(f'UserCRUD[UPDATE_USER] Error: {exc}')
            return f'Update Error'

    def delete_user(self, id):
        try:
            UserModel.query.filter(UserModel.id == id).delete()
            db.session.commit()
            return f'User successfully deleted'
        except Exception as exc:
            print(f'UserCRUD[DELETE_USER] Error: {exc}')
            return f'Delete Error'
