"""banning support

Revision ID: 804005e79950
Revises: 0c9fd367e56b
Create Date: 2019-08-16 21:34:36.679754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '804005e79950'
down_revision = '0c9fd367e56b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('banned', sa.Boolean(), nullable=False, server_default='0'))
        batch_op.add_column(sa.Column('ip_address', sa.String(length=100), nullable=False, server_default=''))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.drop_column('ip_address')
        batch_op.drop_column('banned')

    # ### end Alembic commands ###