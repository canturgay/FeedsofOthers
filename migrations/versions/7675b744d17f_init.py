"""init

Revision ID: 7675b744d17f
Revises: 
Create Date: 2021-12-02 16:06:45.396848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7675b744d17f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    op.create_table('tweet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=100), nullable=True),
    sa.Column('content', sa.String(length=240), nullable=True),
    sa.Column('hashtags', sa.String(length=240), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_name', sa.String(length=15), nullable=True),
    sa.Column('tweet_url', sa.String(length=23), nullable=True),
    sa.Column('contained_url', sa.String(length=100), nullable=True),
    sa.Column('quoted_id', sa.Integer(), nullable=True),
    sa.Column('quoted_user_id', sa.Integer(), nullable=True),
    sa.Column('quoted_hashtags', sa.String(length=240), nullable=True),
    sa.Column('quoted_user_name', sa.String(length=15), nullable=True),
    sa.Column('quoted_url', sa.String(length=23), nullable=True),
    sa.Column('quoted_content', sa.String(length=240), nullable=True),
    sa.Column('quoted_status_contained_url', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oauth_token', sa.String(length=100), nullable=True),
    sa.Column('oauth_token_secret', sa.String(length=100), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('last_sync', sa.TIMESTAMP(), nullable=True),
    sa.Column('authenticated', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('tag_name', sa.String(), nullable=False),
    sa.Column('tweet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tag_name'], ['tag.name'], ),
    sa.ForeignKeyConstraint(['tweet_id'], ['tweet.id'], ),
    sa.PrimaryKeyConstraint('tag_name', 'tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('user')
    op.drop_table('tweet')
    op.drop_table('tag')
    # ### end Alembic commands ###
