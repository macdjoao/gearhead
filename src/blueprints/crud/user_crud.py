from src.blueprints.models.user_model import UserModel
from src.ext.database import db


class UserCRUD:

    def create_user(self, payload):
        try:
            user = UserModel(email=payload['email'], first_name=payload['first_name'],
                             last_name=payload['last_name'], password=payload['password'])

            db.session.add(user)
            db.session.commit()

            return f'User successfully created: {user}'

        except Exception as exc:
            return f'Error: {exc}'
