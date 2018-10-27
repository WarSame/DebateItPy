"""Fixed relationships?

Revision ID: 6eac98a6440b
Revises: 509fd8ebe4ee
Create Date: 2018-10-27 19:55:27.074836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6eac98a6440b'
down_revision = '509fd8ebe4ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_Communities_update_date'), 'Communities', ['update_date'], unique=False)
    op.create_index(op.f('ix_Debates_update_date'), 'Debates', ['update_date'], unique=False)
    op.create_index(op.f('ix_Posts_update_date'), 'Posts', ['update_date'], unique=False)
    op.create_index(op.f('ix_Users_update_date'), 'Users', ['update_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Users_update_date'), table_name='Users')
    op.drop_index(op.f('ix_Posts_update_date'), table_name='Posts')
    op.drop_index(op.f('ix_Debates_update_date'), table_name='Debates')
    op.drop_index(op.f('ix_Communities_update_date'), table_name='Communities')
    # ### end Alembic commands ###