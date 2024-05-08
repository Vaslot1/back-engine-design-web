"""delete column from variables

Revision ID: 50777e3854f4
Revises: c4869902f079
Create Date: 2024-05-06 22:33:58.842976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50777e3854f4'
down_revision: Union[str, None] = 'c4869902f079'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass
    # op.drop_column('variables', 'calculated')


def downgrade() -> None:
    pass
    # op.add_column('variables', sa.Column('calculated',sa.Boolean, nullable=False))
