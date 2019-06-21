"""empty message

Revision ID: 5d36ebeedfec
Revises: bf91bc966825
Create Date: 2019-06-21 16:34:28.367545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d36ebeedfec'
down_revision = 'bf91bc966825'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('skill', sa.String(length=120), nullable=True),
    sa.Column('resume', sa.String(length=140), nullable=True),
    sa.Column('page', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('skills')
    # ### end Alembic commands ###