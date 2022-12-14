"""new fields in user model

Revision ID: 38fc032c43be
Revises: 9862cea4dd13
Create Date: 2022-10-06 17:55:04.315477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38fc032c43be'
down_revision = '9862cea4dd13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
