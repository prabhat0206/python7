"""empty message

Revision ID: 843794e7734b
Revises: 5ddb38af95db
Create Date: 2021-12-21 16:57:48.883800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '843794e7734b'
down_revision = '5ddb38af95db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('trending', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('movie', 'trending')
    # ### end Alembic commands ###
