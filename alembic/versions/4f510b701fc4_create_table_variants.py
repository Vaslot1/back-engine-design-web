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
    pass

def downgrade():
    pass