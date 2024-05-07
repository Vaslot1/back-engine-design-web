"""create table engines

Revision ID: da229888f3d3
Revises: 170a24d19926
Create Date: 2024-05-06 21:02:19.647728

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da229888f3d3'
down_revision: Union[str, None] = '170a24d19926'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass

def downgrade():
    pass
