"""membuat tabel

Revision ID: 77fae5f6fc81
Revises: 9f71752e5b6e
Create Date: 2021-08-03 13:27:17.812161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '77fae5f6fc81'
down_revision = '9f71752e5b6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matakuliah', sa.Column('dosen_pengampu', sa.String(length=60), nullable=False))
    op.drop_column('matakuliah', 'dosen_pengampus')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matakuliah', sa.Column('dosen_pengampus', mysql.VARCHAR(length=60), nullable=False))
    op.drop_column('matakuliah', 'dosen_pengampu')
    # ### end Alembic commands ###