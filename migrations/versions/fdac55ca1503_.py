"""empty message

Revision ID: fdac55ca1503
Revises: f7c10f91c283
Create Date: 2023-06-07 22:18:43.909935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdac55ca1503'
down_revision = 'f7c10f91c283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('files', schema=None) as batch_op:
        batch_op.drop_column('size')

    # ### end Alembic commands ###