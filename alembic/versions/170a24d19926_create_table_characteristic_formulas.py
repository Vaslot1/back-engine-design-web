"""create table characteristic_formulas

Revision ID: 170a24d19926
Revises: 1e2bd16e492f
Create Date: 2024-05-06 21:02:12.292295

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '170a24d19926'
down_revision: Union[str, None] = '1e2bd16e492f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    pass
    # op.create_table(
    #     'characteristic_formulas',
    #     sa.Column('id_characteristic', sa.Integer, sa.ForeignKey('characteristics.id'), primary_key=True),
    #     sa.Column('id_formula', sa.Integer, sa.ForeignKey('formula.id'), primary_key=True),
    #     sa.UniqueConstraint('id_characteristic', 'id_formula')
    # )

def downgrade():
    pass
    # op.drop_table('characteristic_formulas')