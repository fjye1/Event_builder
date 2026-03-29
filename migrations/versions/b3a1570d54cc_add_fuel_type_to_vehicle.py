"""add fuel_type to vehicle

Revision ID: b3a1570d54cc
Revises: 23be3b2c7d14
Create Date: 2026-03-29 14:38:02.254481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3a1570d54cc'
down_revision = '23be3b2c7d14'
branch_labels = None
depends_on = None


from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = 'b3a1570d54cc'
down_revision = '23be3b2c7d14'
branch_labels = None
depends_on = None


def upgrade():
    #create enum type first
    fueltype_enum = postgresql.ENUM('ELECTRIC', 'PETROL', 'DIESEL', name='fueltype')
    fueltype_enum.create(op.get_bind())

    #then add columns
    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.add_column(sa.Column('miles_per_gallon', sa.Integer(), nullable=True))
        batch_op.add_column(
            sa.Column(
                'fuel_type',
                sa.Enum('ELECTRIC', 'PETROL', 'DIESEL', name='fueltype'),
                nullable=True  #important if you already have data
            )
        )


def downgrade():
    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.drop_column('fuel_type')
        batch_op.drop_column('miles_per_gallon')

    # drop enum after column is removed
    fueltype_enum = postgresql.ENUM('ELECTRIC', 'PETROL', 'DIESEL', name='fueltype')
    fueltype_enum.drop(op.get_bind())
