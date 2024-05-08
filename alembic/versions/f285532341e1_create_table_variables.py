"""create table variables

Revision ID: f285532341e1
Revises: 48f2589bde72
Create Date: 2024-05-06 21:01:37.570933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f285532341e1'
down_revision: Union[str, None] = '48f2589bde72'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass

def downgrade():
    pass