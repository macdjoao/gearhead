from src.ext.database import db
import sqlalchemy as sa


class Vehicle(db.Model):

    __tablename__ = 'vehicles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    year = sa.Column(sa.Date, nullable=False)
    code = sa.Column(sa.String, nullable=False)
    brand = sa.Column(sa.Integer, sa.ForeignKey('brands.id'))

    def __str__(self):
        return f'\nname: {self.name}\nyear: {self.year}\ncode: {self.code}\nbrand: {self.brand}'
