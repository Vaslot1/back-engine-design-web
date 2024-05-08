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
    pass

def downgrade():
    pass