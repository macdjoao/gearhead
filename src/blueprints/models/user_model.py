from src.ext.database import db
import sqlalchemy as sa


class UserModel(db.Model):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)

    def __str__(self):
        return f'\nemail: {self.email}\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\nis_active: {self.is_active}'
