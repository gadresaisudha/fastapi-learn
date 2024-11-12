"""add foriegn key to posts table

Revision ID: 8caaca2be473
Revises: add341fdae9c
Create Date: 2024-11-11 17:31:54.940201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8caaca2be473'
down_revision: Union[str, None] = 'add341fdae9c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk','posts',"users",
                          ["owner_id"],["id"],ondelete='CASCADE')


def downgrade():
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    
