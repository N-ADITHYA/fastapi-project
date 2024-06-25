"""Adding a content column to a post tabble 

Revision ID: 548950a0d941
Revises: aca94a7d137d
Create Date: 2024-06-25 14:32:50.264415

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '548950a0d941'
down_revision: Union[str, None] = 'aca94a7d137d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass