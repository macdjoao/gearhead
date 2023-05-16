from src.ext.database import db
import sqlalchemy as sa
from werkzeug.security import check_password_hash


class UserModel(db.Model):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)

    def __str__(self):
        return f'email: {self.email} ; first_name: {self.first_name} ; last_name: {self.last_name} ; is_active: {self.is_active}'

    def verify_password(self, password):
        return check_password_hash(self.password, password)
