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
            return f'Error: {exc}'
