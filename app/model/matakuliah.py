from app import db
from app.model.dosen import Dosen

class Matakuliah(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    kode_kuliah = db.Column(db.String(30), nullable=False)
    nama_mata_kuliah = db.Column(db.String(60), nullable=False)
    jumlah_sks = db.Column(db.BigInteger, nullable=False)
    dosen_pengampu = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<Matakuliah {}>'.format(self.name)