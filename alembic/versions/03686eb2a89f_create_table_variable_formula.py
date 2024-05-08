"""create table variable_formula

Revision ID: 03686eb2a89f
Revises: 449aa15b98ef
Create Date: 2024-05-06 21:01:56.630312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03686eb2a89f'
down_revision: Union[str, None] = '449aa15b98ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass
    # op.create_table(
    #     'variable_formula',
    #     sa.Column('id_variable', sa.Integer, sa.ForeignKey('variables.id'), primary_key=True),
    #     sa.Column('id_formula', sa.Integer, sa.ForeignKey('formula.id'), primary_key=True),
    #     sa.UniqueConstraint('id_variable', 'id_formula')
    # )

def downgrade():
    pass
    # op.drop_table('variable_formula')