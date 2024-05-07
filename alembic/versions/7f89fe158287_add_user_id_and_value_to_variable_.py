"""add user_id and value to variable_formula

Revision ID: 7f89fe158287
Revises: 50777e3854f4
Create Date: 2024-05-07 23:01:57.500518

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f89fe158287'
down_revision: Union[str, None] = '50777e3854f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('variable_formula', sa.Column("user_id", sa.Integer, nullable=False,
                primary_key=True))
    op.add_column('variable_formula', sa.Column("value", sa.Float))


def downgrade():
    op.drop_column('variable_formula', 'user_id')
    op.drop_column('variable_formula', 'value')
