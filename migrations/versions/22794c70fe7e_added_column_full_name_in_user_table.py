"""Added column full_name in user table

Revision ID: 22794c70fe7e
Revises: 4da9e1ec1000
Create Date: 2020-12-09 16:07:32.344075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "22794c70fe7e"
down_revision = "4da9e1ec1000"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("full_name", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "full_name")
    # ### end Alembic commands ###
