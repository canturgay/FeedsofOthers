"""Initial migration.

Revision ID: 42fe22e2314a
Revises: 
Create Date: 2021-11-26 15:59:20.938384

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '42fe22e2314a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('oauth_token', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('oauth_secret', sa.String(length=100), nullable=True))
    op.drop_column('user', 'last_load')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_load', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.drop_column('user', 'oauth_secret')
    op.drop_column('user', 'oauth_token')
    # ### end Alembic commands ###