"""empty message

Revision ID: 4db14c81526c
Revises: ed9d2c5ae1d2
Create Date: 2017-02-25 20:43:00.766401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4db14c81526c'
down_revision = 'ed9d2c5ae1d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
