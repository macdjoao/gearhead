from src.ext.database import db
import sqlalchemy as sa


class PartModel(db.Model):

    __tablename__ = 'parts'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    amount = sa.Column(sa.Integer, default=0)
    code = sa.Column(sa.String, nullable=False)
    vehicle = sa.Column(sa.String, sa.ForeignKey('vehicles.id'))

    def __str__(self):
        return f'\nname: {self.name}\namount: {self.amount}\ncode: {self.code}\nvehicle: {self.vehicle}'
