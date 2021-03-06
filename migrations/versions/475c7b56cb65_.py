"""empty message

Revision ID: 475c7b56cb65
Revises: 9fb381df53dc
Create Date: 2017-06-21 00:41:18.071455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '475c7b56cb65'
down_revision = '9fb381df53dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
