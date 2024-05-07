"""create teble users

Revision ID: 48f2589bde72
Revises: 065a93e5fb52
Create Date: 2024-05-06 21:01:14.775262

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48f2589bde72'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('full_name', sa.String(150), nullable=False),
        sa.Column('password', sa.String, nullable=False),
        sa.Column('user_group', sa.String(20)),
        sa.Column('role', sa.String(10)),
        sa.UniqueConstraint('id')
    )

def downgrade():
    op.drop_table('users')

