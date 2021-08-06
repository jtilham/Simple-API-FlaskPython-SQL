from app.model.matakuliah import Matakuliah

from app import response, app, db
from flask import request, jsonify,abort

import math


def index():
    try:
        matakuliah = Matakuliah.query.all()
        

        data = formatarray(matakuliah)
        return response.success(data, "success")
    except Exception as e:
        print(e)


def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))
    
    return array


def singleObject(data):
    data = {
        'kode_kuliah' : data.kode_kuliah,
        'nama_mata_kuliah' : data.nama_mata_kuliah,
        'jumlah_sks' : data.jumlah_sks,
        'dosen_pengampu' : data.dosen_pengampu,
    }

    return data

def save():
    try:
        kode_kuliah = request.form.get('kode_kuliah')
        nama_mata_kuliah = request.form.get('nama_mata_kuliah')
        jumlah_sks = request.form.get('jumlah_sks')
        dosen_pengampu = request.form.get('dosen_pengampu')

        input = [{
            'kode_kuliah':kode_kuliah,
            'nama_mata_kuliah':nama_mata_kuliah,
            'jumlah_sks':jumlah_sks,
            'dosen_pengampu':dosen_pengampu
        }]
        

        matakuliahs = Matakuliah(kode_kuliah=kode_kuliah, nama_mata_kuliah=nama_mata_kuliah, jumlah_sks=jumlah_sks, dosen_pengampu=dosen_pengampu)
        db.session.add(matakuliahs)
        db.session.commit()

        return response.success(input, 'Sukses menambahkan Data Matakuliah')

    except Exception as e:
        print(e)


def detail(id):
    try:
        matkul = Matakuliah.query.filter(Matakuliah.id==id)
        if not matkul:
            return response.badRequest([], 'Data matakuliah Kosong... ')

        datamatakuliah = formatarray(matkul)
        
        return response.success(datamatakuliah, "success")
    
    except Exception as e:
        print(e)


def ubah(id):
    try:
        kode_kuliah = request.form.get('kode_kuliah')
        nama_mata_kuliah = request.form.get('nama_mata_kuliah')
        jumlah_sks = request.form.get('jumlah_sks')
        dosen_pengampu = request.form.get('dosen_pengampu')

        input = [{
            'kode_kuliah':kode_kuliah,
            'nama_mata_kuliah':nama_mata_kuliah,
            'jumlah_sks':jumlah_sks,
            'dosen_pengampu':dosen_pengampu
        }]

        matakuliah = Matakuliah.query.filter_by(id=id).first()

        matakuliah.kode_kuliah = kode_kuliah
        matakuliah.nama_mata_kuliah = nama_mata_kuliah
        matakuliah.jumlah_sks = jumlah_sks
        matakuliah.dosen_pengampu = dosen_pengampu

        db.session.commit()

        return response.success(input, 'Sukses Update Data!')
    
    except Exception as e:
        print(e)


def hapus(id):
    try:
        matakuliah = Matakuliah.query.filter_by(id=id).first()
        if not matakuliah:
            return response.badRequest([], 'Data Dosen Kosong... ')
            
        db.session.delete(matakuliah)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data!')
    except Exception as e:
        print(e)