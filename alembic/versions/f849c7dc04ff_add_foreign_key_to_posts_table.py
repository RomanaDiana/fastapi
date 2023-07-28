"""add foreign key to posts table

Revision ID: f849c7dc04ff
Revises: b76e3f1693db
Create Date: 2023-07-28 16:00:32.035061

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f849c7dc04ff'
down_revision = 'b76e3f1693db'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table="posts",
                          referent_table="users", local_cols=["owner_id"], remote_cols=["id"],
                          ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
