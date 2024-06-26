"""integrate schema from dataset

Revision ID: 96f72bedd683
Create Date: 2024-04-27 15:24:57.724173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects.postgresql import TSVECTOR


# revision identifiers, used by Alembic.
revision: str = '96f72bedd683'
down_revision: Union[str, None] = '018fdd3b3a8e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('question_answer',
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('embedding', sa.ARRAY(sa.FLOAT(32)), nullable=False),
    sa.Column('answer_class', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['answer_class'], ['answers.id'], ),
    sa.PrimaryKeyConstraint('question')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_answer')
    op.drop_table('answers')
    # ### end Alembic commands ###
