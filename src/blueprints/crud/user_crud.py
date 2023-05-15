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
            return f'User successfully created: {user}'
        except Exception as exc:
            return f'UserCRUD[CREATE_USER] Error: {exc}'

    def read_users(self):
        try:
            query = UserModel.query.all()
            schema = UserSchema(many=True)
            response = schema.jsonify(query)
            return f'Users: {response}'
        except Exception as exc:
            return f'UserCRUD[READ_USERS] Error: {exc}'
