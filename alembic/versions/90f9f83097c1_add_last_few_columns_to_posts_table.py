"""add last few columns to posts table

Revision ID: 90f9f83097c1
Revises: f849c7dc04ff
Create Date: 2023-07-28 16:18:38.366402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90f9f83097c1'
down_revision = 'f849c7dc04ff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",
                  sa.Column("published", sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column("posts",
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False,
                            server_default=sa.text("NOW()")),)
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
