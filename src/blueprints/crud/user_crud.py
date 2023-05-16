from src.blueprints.models.user_model import UserModel
from src.ext.database import db
from werkzeug.security import generate_password_hash
from src.blueprints.schemas.user_schema import UserSchema


class UserCRUD:

    def create_user(self, payload):
        try:
            user = UserModel(email=payload['email'], first_name=payload['first_name'],
                             last_name=payload['last_name'], password=payload['password'])
            user.password = generate_password_hash(user.password)
            db.session.add(user)
            db.session.commit()
            schema = UserSchema()
            return f'User successfully created: {schema.dump(user)}'
        except Exception as exc:
            print(f'UserCRUD[CREATE_USER] Error: {exc}')
            return f'Create Error'

    def read_user(self, id):
        try:
            user = UserModel.query.filter_by(id=id).first()
            schema = UserSchema()
            return f'User: {schema.dump(user)}'
        except Exception as exc:
            print(f'UserCRUD[READ_USER] Error: {exc}')
            return f'Read Error'

    def read_users(self):
        try:
            users = UserModel.query.all()
            schema = UserSchema(many=True)
            return f'User: {schema.dump(users)}'
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
            UserModel.query.filter_by(id=id).delete()
            db.session.commit()
            return f'User successfully deleted.'
        except Exception as exc:
            print(f'UserCRUD[DELETE_USER] Error: {exc}')
            return f'Delete Error'
