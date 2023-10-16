"""Create Posts Table

Revision ID: fa50fed410a2
Revises:
Create Date: 2022-01-27 08:54:58.651298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa50fed410a2'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=('now()'), nullable=False),
        sa.Column('fname', sa.String(),nullable=False),
        sa.Column('lname', sa.String(),nullable=False),
        sa.Column('email', sa.String(),nullable=False),
        sa.Column('password', sa.String(),nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'))

    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('published', sa.Boolean(), server_default='True', nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'))

    op.create_table('votes',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'post_id'))

    op.create_table('gps',
        sa.Column('gps_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('lat', sa.String(),nullable=False),
        sa.Column('lng', sa.String(),nullable=False),
        sa.PrimaryKeyConstraint('gps_id'))

    op.create_table('clubs',
        sa.Column('club_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=('now()'), nullable=False),
        sa.Column('name', sa.String(),nullable=False),
        sa.Column('logo', sa.String(),nullable=True),
        sa.Column('email', sa.String(),nullable=False),
        sa.Column('pri_contact', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['pri_contact'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('club_id'))

    op.create_table('events',
        sa.Column('event_id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=('now()'), nullable=False),
        sa.Column('hostedby', sa.Integer(),nullable=False),
        sa.Column('title', sa.String(),nullable=True),
        sa.Column('description', sa.String(),nullable=False),
        sa.Column('event_start', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('event_end'  , sa.TIMESTAMP(timezone=True), nullable=True),
        sa.Column('publish', sa.Boolean(), server_default='True', nullable=False),
        sa.ForeignKeyConstraint(['hostedby'], ['clubs.club_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('event_id'))
    pass

def downgrade():
    op.drop_table('gps')
    op.drop_table('votes')
    op.drop_table('posts')
    op.drop_table('events')
    op.drop_table('clubs')
    op.drop_table('users')
    pass
