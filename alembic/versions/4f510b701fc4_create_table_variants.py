"""create table variants

Revision ID: 4f510b701fc4
Revises: da229888f3d3
Create Date: 2024-05-06 21:02:26.975810

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import REAL
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f510b701fc4'
down_revision: Union[str, None] = 'da229888f3d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'variants',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('voltage', float),
        sa.Column('power', float),
        sa.Column('cnt_pole', sa.Integer),
        sa.Column('solved', sa.Boolean),
        sa.Column('slide', float),
        sa.Column('class_hr', sa.String(1)),
        sa.Column('engine', sa.Integer, sa.ForeignKey('engines.id')),
        sa.UniqueConstraint('id')
    )

def downgrade():
    op.drop_table('variants')