"""add columns to posts table

Revision ID: ce58b523a231
Revises: eeb18f3337b7
Create Date: 2024-11-11 17:04:41.532635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce58b523a231'
down_revision: Union[str, None] = 'eeb18f3337b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')

