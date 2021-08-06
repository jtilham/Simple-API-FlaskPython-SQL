"""membuat tabel

Revision ID: 9ca2091ec2c2
Revises: 574e2f8f6543
Create Date: 2021-08-03 12:32:52.371025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ca2091ec2c2'
down_revision = '574e2f8f6543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matakuliah',
    sa.Column('kode_kuliah', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nama_mata_kuliah', sa.String(length=60), nullable=False),
    sa.Column('jumlah_sks', sa.BigInteger(), nullable=False),
    sa.Column('dosen_satu', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['dosen_satu'], ['dosen.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('kode_kuliah')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matakuliah')
    # ### end Alembic commands ###
