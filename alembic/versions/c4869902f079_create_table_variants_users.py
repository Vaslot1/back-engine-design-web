"""create table variants_users

Revision ID: c4869902f079
Revises: 4f510b701fc4
Create Date: 2024-05-06 21:02:32.065648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4869902f079'
down_revision: Union[str, None] = '4f510b701fc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'variants_users',
        sa.Column('id_variant', sa.Integer, sa.ForeignKey('variants.id'), primary_key=True),
        sa.Column('id_user', sa.Integer, sa.ForeignKey('users.id'), primary_key=True),
        sa.UniqueConstraint('id_variant', 'id_user')
    )

def downgrade():
    op.drop_table('variants_users')