"""add user table

Revision ID: b76e3f1693db
Revises: bc130e285c18
Create Date: 2023-07-28 15:42:39.354235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b76e3f1693db'
down_revision = 'bc130e285c18'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
