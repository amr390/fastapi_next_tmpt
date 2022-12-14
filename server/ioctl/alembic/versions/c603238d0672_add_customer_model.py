"""add customer model

Revision ID: c603238d0672
Revises: ebec570a7f9a
Create Date: 2022-10-28 18:28:08.374090

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c603238d0672'
down_revision = 'ebec570a7f9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_first_name'), 'customer', ['first_name'], unique=False)
    op.create_index(op.f('ix_customer_id'), 'customer', ['id'], unique=False)
    op.create_index(op.f('ix_customer_last_name'), 'customer', ['last_name'], unique=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_index(op.f('ix_customer_last_name'), table_name='customer')
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.drop_index(op.f('ix_customer_first_name'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###
