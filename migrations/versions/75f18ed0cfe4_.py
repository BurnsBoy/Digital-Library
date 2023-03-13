"""empty message

Revision ID: 75f18ed0cfe4
Revises: 6829a8a2f166
Create Date: 2023-03-12 20:45:58.902029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '75f18ed0cfe4'
down_revision = '6829a8a2f166'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('isbn',
               existing_type=sa.NUMERIC(precision=17, scale=0),
               type_=sa.Numeric(precision=13, scale=0),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.alter_column('isbn',
               existing_type=sa.Numeric(precision=13, scale=0),
               type_=sa.NUMERIC(precision=17, scale=0),
               existing_nullable=True)

    # ### end Alembic commands ###