"""empty message

Revision ID: 1c3524e7cf32
Revises: 
Create Date: 2024-06-05 17:24:54.308996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c3524e7cf32'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('unique', sa.UUID(), nullable=False),
    sa.Column('path', sa.TEXT(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('bundle_hash', sa.String(length=256), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path', 'bundle_hash', name='_path_bundle_hash'),
    sa.UniqueConstraint('unique')
    )
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_file_created'), ['created'], unique=False)

    op.create_table('download',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('bundle_hash', sa.String(length=256), nullable=False),
    sa.Column('download_count', sa.Integer(), nullable=False),
    sa.Column('download_max', sa.Integer(), nullable=True),
    sa.Column('last_downloaded', sa.DateTime(timezone=True), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('download', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_download_created'), ['created'], unique=False)
        batch_op.create_index(batch_op.f('ix_download_file_id'), ['file_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_download_last_downloaded'), ['last_downloaded'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('download', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_download_last_downloaded'))
        batch_op.drop_index(batch_op.f('ix_download_file_id'))
        batch_op.drop_index(batch_op.f('ix_download_created'))

    op.drop_table('download')
    with op.batch_alter_table('file', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_file_created'))

    op.drop_table('file')
    # ### end Alembic commands ###