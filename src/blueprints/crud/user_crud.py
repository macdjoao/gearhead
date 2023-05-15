from src.blueprints.models.user_model import UserModel
from src.ext.database import db


class UserCRUD:

    def create_user(self, email, first_name, last_name, password):
        try:
            user = UserModel(email=email, first_name=first_name,
                             last_name=last_name, password=password)

            db.session.add(user)
            db.session.commit()

            return f'User successfully created: {user}'

        except Exception as exc:
            return f'Error: {exc}'
