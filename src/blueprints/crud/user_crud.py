from src.blueprints.models.user_model import UserModel
from src.ext.database import db
from werkzeug.security import generate_password_hash
from src.blueprints.schemas.user_schema import UserSchema


class UserCRUD:

    def create_user(self, payload: dict):
        schema = UserSchema()
        try:
            email = payload['email'].lower()
            first_name = payload['first_name'].capitalize()
            last_name = payload['last_name'].capitalize()
            password = generate_password_hash(payload['password'])
            user = UserModel(email=email, first_name=first_name,
                             last_name=last_name, password=password)
            db.session.add(user)
            db.session.commit()
            return schema.dump(user)
        except Exception as exc:
            print(f'UserCRUD[CREATE_USER] Error: {exc}')
            return f'Create Error.'

    def read_user(self, id: int):
        schema = UserSchema()
        try:
            user = UserModel.query.get(id)
            if user is None:
                return 'User not found', 404
            return schema.dump(user)
        except Exception as exc:
            print(f'UserCRUD[READ_USER] Error: {exc}')
            return f'Read Error.'

    def read_users(self):
        schema = UserSchema(many=True)
        try:
            users = UserModel.query.all()
            if users is None:
                return 'Users not found', 404
            return schema.dump(users)
        except Exception as exc:
            print(f'UserCRUD[READ_USERS] Error: {exc}')
            return f'Read Error.'

    def update_user(self, id: int, payload: dict):
        try:
            user = UserModel.query.get(id)
            if user is None:
                return 'User not found', 404
            if 'email' in payload:
                user.email = payload['email'].lower()
            if 'first_name' in payload:
                user.first_name = payload['first_name'].capitalize()
            if 'last_name' in payload:
                user.last_name = payload['last_name'].capitalize()
            if 'password' in payload:
                user.password = generate_password_hash(payload['password'])
            if 'is_active' in payload:
                user.is_active = payload['is_active']
            db.session.commit()
            return f'User successfully updated'
        except Exception as exc:
            print(f'UserCRUD[UPDATE_USER] Error: {exc}')
            return f'Update Error.'

    def delete_user(self, id: int):
        try:
            user = UserModel.query.get(id)
            if user is None:
                return 'User not found', 404
            UserModel.query.filter_by(id=id).delete()
            db.session.commit()
            return f'User successfully deleted.'
        except Exception as exc:
            print(f'UserCRUD[DELETE_USER] Error: {exc}')
            return f'Delete Error.'
