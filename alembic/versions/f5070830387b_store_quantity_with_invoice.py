"""Store quantity with invoice

Revision ID: f5070830387b
Revises: 25165517c582
Create Date: 2020-01-07 17:51:51.217049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5070830387b'
down_revision = '25165517c582'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('productsxinvoices', sa.Column('count', sa.Integer(), nullable=True, server_default="1"))
    op.alter_column('productsxinvoices', 'count', server_default=None)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('productsxinvoices', 'count')
    # ### end Alembic commands ###