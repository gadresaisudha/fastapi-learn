"""add remaining columns to posts table

Revision ID: e2d9615814cb
Revises: 8caaca2be473
Create Date: 2024-11-11 17:44:42.048901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2d9615814cb'
down_revision: Union[str, None] = '8caaca2be473'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean(),server_default='True',nullable=False))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False))


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')