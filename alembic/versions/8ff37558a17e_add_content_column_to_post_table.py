"""add content column to post table

Revision ID: 8ff37558a17e
Revises: 13f3977b8969
Create Date: 2024-07-10 14:39:23.645131

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ff37558a17e'
down_revision: Union[str, None] = '13f3977b8969'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(), nullable=False)
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
