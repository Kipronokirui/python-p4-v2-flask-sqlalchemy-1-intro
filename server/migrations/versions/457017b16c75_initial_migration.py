"""Initial migration.

Revision ID: 457017b16c75
Revises: 
Create Date: 2024-04-03 22:37:40.319256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '457017b16c75'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###
