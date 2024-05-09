"""create table characteristics

Revision ID: 1e2bd16e492f
Revises: 03686eb2a89f
Create Date: 2024-05-06 21:02:04.166777

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e2bd16e492f'
down_revision: Union[str, None] = '03686eb2a89f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'engines',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(150), nullable=False),
        sa.UniqueConstraint('id')
    )
    op.create_table(
        'characteristics',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(200), nullable=False),
        sa.Column('engine', sa.Integer, sa.ForeignKey('engines.id')),
        sa.UniqueConstraint('id')
    )

    op.create_table(
        'variants',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('voltage', sa.Float),
        sa.Column('power', sa.Float),
        sa.Column('cnt_pole', sa.Integer),
        sa.Column('solved', sa.Boolean),
        sa.Column('slide', sa.Float),
        sa.Column('class_hr', sa.String(1)),
        sa.Column('engine_id', sa.Integer, sa.ForeignKey('engines.id')),
        sa.UniqueConstraint('id')
    )
    op.create_table(
        'variants_users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('id_variant', sa.Integer, sa.ForeignKey('variants.id')),
        sa.Column('id_user', sa.Integer, sa.ForeignKey('users.id'))
    )
    op.create_table(
        'vars_initial_data',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('short_name', sa.String(25), nullable=False),
        sa.Column('value', sa.Float),
        sa.Column('id_variant_user', sa.Integer, sa.ForeignKey('variants_users.id')),
        sa.UniqueConstraint('id')
    )
    op.create_table(
        'formulas',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('string_res', sa.String(50)),
        sa.Column('number', sa.Integer),
        sa.Column('dim', sa.String(10)),
        sa.Column('id_char', sa.Integer, sa.ForeignKey('characteristics.id')),
        sa.UniqueConstraint('id')
    )


def downgrade():
    op.drop_table('vars_initial_data')
    op.drop_table('variants_users')
    op.drop_table('variants')
    op.drop_table('formulas')
    op.drop_table('characteristics')
    op.drop_table('engines')
