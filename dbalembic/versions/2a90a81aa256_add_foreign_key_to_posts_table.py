"""Add foreign key to posts table

Revision ID: 2a90a81aa256
Revises: 2870207e2f7c
Create Date: 2024-06-25 15:08:51.781600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a90a81aa256'
down_revision: Union[str, None] = '2870207e2f7c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
