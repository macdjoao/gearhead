from src.ext.database import db
import sqlalchemy as sa


class Brand(db.Model):

    __tablename__ = 'brands'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    code = sa.Column(sa.String, nullable=False, unique=True)

    def __str__(self):
        return f'\nname: {self.name}\ncode: {self.code}'
