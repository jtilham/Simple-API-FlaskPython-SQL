"""membuat tabel

Revision ID: 54e56d56cfe3
Revises: 5f49c8c962bc
Create Date: 2021-08-03 13:24:11.456379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '54e56d56cfe3'
down_revision = '5f49c8c962bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('matakuliah', 'dosen_pengampu',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.drop_constraint('matakuliah_ibfk_1', 'matakuliah', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('matakuliah_ibfk_1', 'matakuliah', 'dosen', ['dosen_pengampu'], ['id'], ondelete='CASCADE')
    op.alter_column('matakuliah', 'dosen_pengampu',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    # ### end Alembic commands ###
