from src.ext.database import db
import sqlalchemy as sa


class User(db.Model):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String, unique=True, nullable=False)
    first_name = sa.Column(sa.String, nullable=False)
    last_name = sa.Column(sa.String, nullable=False)
    password = sa.Column(sa.String, nullable=False)
    is_active = sa.Column(sa.Boolean, default=True)

    def __str__(self):
        return f'\nemail: {self.email}\nfirst_name: {self.first_name}\nlast_name: {self.last_name}\nis_active: {self.is_active}'


class Brand(db.Model):

    __tablename__ = 'brands'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False, unique=True)
    code = sa.Column(sa.String, nullable=False, unique=True)

    def __str__(self):
        return f'\nname: {self.name}\ncode: {self.code}'


class Vehicle(db.Model):

    __tablename__ = 'vehicles'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    year = sa.Column(sa.Date, nullable=False)
    code = sa.Column(sa.String, nullable=False)
    brand = sa.Column(sa.Integer, sa.ForeignKey('brands.id'))

    def __str__(self):
        return f'\nname: {self.name}\nyear: {self.year}\ncode: {self.code}\nbrand: {self.brand}'


class Part(db.Model):

    __tablename__ = 'parts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    amount = sa.Column(sa.Integer, default=0)
    code = sa.Column(sa.String, nullable=False)
    vehicle = sa.Column(sa.String, sa.ForeignKey('vehicles.id'))

    def __str__(self):
        return f'\nname: {self.name}\namount: {self.amount}\ncode: {self.code}\nvehicle: {self.vehicle}'
