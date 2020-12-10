"""Added relationship whit user in table purchase

Revision ID: b0c3dd0f3434
Revises: d8724a5e7b34
Create Date: 2020-12-10 03:47:20.186750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b0c3dd0f3434"
down_revision = "d8724a5e7b34"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("purchase", sa.Column("user_id", sa.Integer(), nullable=False))
    op.create_foreign_key(None, "purchase", "user", ["user_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "purchase", type_="foreignkey")
    op.drop_column("purchase", "user_id")
    # ### end Alembic commands ###
