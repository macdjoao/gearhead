"""empty message

Revision ID: e20781f394bd
Revises: 3315e8ffb16a
Create Date: 2023-05-12 16:17:41.334196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e20781f394bd'
down_revision = '3315e8ffb16a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.add_column(sa.Column('teste', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('brands', schema=None) as batch_op:
        batch_op.drop_column('teste')

    # ### end Alembic commands ###
