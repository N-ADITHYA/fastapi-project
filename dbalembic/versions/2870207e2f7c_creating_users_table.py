"""Creating users table

Revision ID: 2870207e2f7c
Revises: 548950a0d941
Create Date: 2024-06-25 14:43:04.035447

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2870207e2f7c'
down_revision: Union[str, None] = '548950a0d941'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
          sa.Column('id', sa.Integer(), nullable=False),
                   sa.Column('email', sa.String(), nullable=False),
                   sa.Column('password', sa.String(), nullable=False),
                   sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                         server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
