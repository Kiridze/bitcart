"""Add invoice creation time

Revision ID: 2a33595c8b9d
Revises: 427d55a6fd22
Create Date: 2023-02-07 01:57:41.097768

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "2a33595c8b9d"
down_revision = "427d55a6fd22"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("invoices", sa.Column("creation_time", sa.Numeric(precision=36, scale=18), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("invoices", "creation_time")
    # ### end Alembic commands ###
