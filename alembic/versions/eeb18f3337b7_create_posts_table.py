"""create posts table

Revision ID: eeb18f3337b7
Revises: 
Create Date: 2024-11-11 16:41:17.092108

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eeb18f3337b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title',sa.String(),nullable= False))
def downgrade() -> None:
    op.drop_table('posts')
    pass
