"""add content column to posts table

Revision ID: bc130e285c18
Revises: b0b2a87aa047
Create Date: 2023-07-28 15:26:19.414791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc130e285c18'
down_revision = 'b0b2a87aa047'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
