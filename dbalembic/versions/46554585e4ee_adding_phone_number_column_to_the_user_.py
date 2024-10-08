"""Adding phone number column to the user table using autogenerate

Revision ID: 46554585e4ee
Revises: 1068c9a8f9db
Create Date: 2024-06-25 17:45:13.052201

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '46554585e4ee'
down_revision: Union[str, None] = '1068c9a8f9db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')

    # ### end Alembic commands ###
