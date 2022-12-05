"""create token model

Revision ID: 4c35a8333dc7
Revises: 2aec72975d22
Create Date: 2022-11-30 23:59:08.198818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c35a8333dc7'
down_revision = '2aec72975d22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refreshtoken',
    sa.Column('id', sa.VARCHAR(255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('validity_timestamp', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_refreshtoken_id'), 'refreshtoken', ['id'], unique=False)
    op.create_index(op.f('ix_refreshtoken_user_id'), 'refreshtoken', ['user_id'], unique=False)
    op.create_index(op.f('ix_refreshtoken_validity_timestamp'), 'refreshtoken', ['validity_timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_refreshtoken_validity_timestamp'), table_name='refreshtoken')
    op.drop_index(op.f('ix_refreshtoken_user_id'), table_name='refreshtoken')
    op.drop_index(op.f('ix_refreshtoken_id'), table_name='refreshtoken')
    op.drop_table('refreshtoken')
    # ### end Alembic commands ###