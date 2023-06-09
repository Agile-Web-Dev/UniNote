"""is bot nullable

Revision ID: e57c98f6e82b
Revises: cb16188a22d0
Create Date: 2023-05-21 16:06:03.725117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e57c98f6e82b'
down_revision = 'cb16188a22d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.alter_column('is_bot',
               existing_type=sa.BOOLEAN(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.alter_column('is_bot',
               existing_type=sa.BOOLEAN(),
               nullable=False)

    # ### end Alembic commands ###
