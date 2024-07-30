"""empty message

Revision ID: 8d2b8d633509
Revises: 441f66454c4d
Create Date: 2024-07-30 15:31:16.756328

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8d2b8d633509'
down_revision: Union[str, None] = '441f66454c4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('advances', 'description',
               existing_type=sa.VARCHAR(),
               type_=sa.Text(),
               existing_comment='Описание достижения',
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('advances', 'description',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(),
               existing_comment='Описание достижения',
               existing_nullable=False)
    # ### end Alembic commands ###
