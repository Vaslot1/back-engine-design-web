"""create table formula

Revision ID: 449aa15b98ef
Revises: f285532341e1
Create Date: 2024-05-06 21:01:47.825226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '449aa15b98ef'
down_revision: Union[str, None] = 'f285532341e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass

def downgrade():
    pass