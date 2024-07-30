"""empty message

Revision ID: f240e5720016
Revises: 
Create Date: 2024-07-29 18:36:21.835983

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f240e5720016'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('achievements',
    sa.Column('name', sa.String(), nullable=False, comment='Название достижения'),
    sa.Column('number_points', sa.String(), nullable=False, comment='Количество баллов за достижения'),
    sa.Column('description', sa.String(), nullable=False, comment='Описание достижения'),
    sa.Column('id', sa.Uuid(), autoincrement=False, nullable=False, comment='Уникальный идентификатор'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('name', sa.String(), nullable=False, comment='Имя пользователя'),
    sa.Column('language', sa.Enum('RU', 'EN', name='language'), nullable=False, comment='Выбранный пользователем язык'),
    sa.Column('id', sa.Uuid(), autoincrement=False, nullable=False, comment='Уникальный идентификатор'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('achievements')
    # ### end Alembic commands ###
