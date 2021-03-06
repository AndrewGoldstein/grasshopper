"""empty message

Revision ID: 9e99bd1decae
Revises: 4897923f45be
Create Date: 2016-02-22 03:06:38.453605

"""

# revision identifiers, used by Alembic.
revision = '9e99bd1decae'
down_revision = '4897923f45be'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address_city', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('address_country', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('address_line1', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('address_line2', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('address_state', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('address_zip', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('date_of_birth', sa.String(length=30), nullable=True))
    op.add_column('users', sa.Column('gender', sa.String(length=15), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=15), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'date_of_birth')
    op.drop_column('users', 'address_zip')
    op.drop_column('users', 'address_state')
    op.drop_column('users', 'address_line2')
    op.drop_column('users', 'address_line1')
    op.drop_column('users', 'address_country')
    op.drop_column('users', 'address_city')
    ### end Alembic commands ###
