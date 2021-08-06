"""membuat tabel

Revision ID: 5e290df55c45
Revises: 17e15a4e739c
Create Date: 2021-08-03 12:39:59.545040

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e290df55c45'
down_revision = '17e15a4e739c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matakuliah', sa.Column('kode_kuliahh', sa.String(length=30), nullable=False))
    op.drop_column('matakuliah', 'kode_kuliah')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('matakuliah', sa.Column('kode_kuliah', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False))
    op.drop_column('matakuliah', 'kode_kuliahh')
    # ### end Alembic commands ###
