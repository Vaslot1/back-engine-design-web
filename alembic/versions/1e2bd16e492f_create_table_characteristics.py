"""create table characteristics

Revision ID: 1e2bd16e492f
Revises: 03686eb2a89f
Create Date: 2024-05-06 21:02:04.166777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e2bd16e492f'
down_revision: Union[str, None] = '03686eb2a89f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'engines',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.UniqueConstraint('id')
    )
    op.create_table(
        'characteristics',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('engine', sa.Integer, sa.ForeignKey('engines.id')),
        sa.UniqueConstraint('id')
    )


def downgrade():
    op.drop_table('engines')
    op.drop_table('characteristics')