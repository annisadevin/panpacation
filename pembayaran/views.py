from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple

from datetime import date

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def list_villa():
    with connection.cursor() as c:
        c.execute("SELECT * FROM VILLA")
        res = dictfetchall(c)
    
    list_villa = []
    for i in res:
        list_villa.append(i['id_penginapan'])

    return list_villa

def list_kos():
    with connection.cursor() as c:
        c.execute("SELECT * FROM KOS")
        res = dictfetchall(c)
    
    list_kos = []
    for i in res:
        list_kos.append(i['id_penginapan'])

    return list_kos

def list_apart():
    with connection.cursor() as c:
        c.execute("SELECT * FROM APARTEMEN")
        res = dictfetchall(c)
    
    list_apart = []
    for i in res:
        list_apart.append(i['id_penginapan'])

    return list_apart

def check_jenis(id_penginapan):
    jenis = ''
    for i in list_villa():
        if i == id_penginapan:
            jenis = 'Villa'

    for i in list_kos():
        if i == id_penginapan:
            jenis = 'Kosan'
    
    for i in list_apart():
        if i == id_penginapan:
            jenis = 'Apartement'
    
    return jenis

def buatpesanan(request, id_penginapan, tgl_checkin, tgl_checkout, total_penginap):
    namap = request.POST.get('namapemesan', None)
    jenis = request.POST.get('jenistest', None)

    # with connection.cursor() as c:
    #     c.execute("SELECT * FROM PENGGUNA")
    #     data_pemesan = dictfetchall(c)
    
    with connection.cursor() as c:
        c.execute("SELECT * FROM TEMPAT_PENGINAPAN where id_penginapan = '"+ id_penginapan +"'")
        res = dictfetchall(c)

    nama_penginapan = res[0]['nama']
    jenis_penginapan = check_jenis(id_penginapan)

    with connection.cursor() as c:
        c.execute("SELECT * FROM TRANSAKSI")
        res = dictfetchall(c)

    id_transaksi = res[len(res)-1]['id_transaksi']

    with connection.cursor() as c:
        c.execute("SELECT id_transaksi_penginapan FROM TRANSAKSI_PENGINAPAN where id_transaksi = '"+ id_transaksi +"'")
        res = dictfetchall(c)

    id_transaksi_penginapan = res[0]['id_transaksi_penginapan']

    data_transaksi = {}
    if jenis_penginapan == 'Villa':
        with connection.cursor() as c:
            c.execute("SELECT * FROM PILIHAN_VILLA NATURAL JOIN VILLA where id_transaksi_penginapan = '"+ id_transaksi_penginapan +"'")
            data_transaksi = dictfetchall(c)

    elif jenis_penginapan == 'Kosan':
        with connection.cursor() as c:
            c.execute("SELECT * FROM PILIHAN_KOS_ROOM PK JOIN KOS_ROOM KR ON PK.id_kode_room = KR.kode_room where id_transaksi_penginapan = '"+ id_transaksi_penginapan +"' and PK.id_kos = KR.id_kos")
            data_transaksi = dictfetchall(c)

    elif jenis_penginapan == 'Apartement':
        with connection.cursor() as c:
            c.execute("SELECT * FROM PILIHAN_APARTEMEN_ROOM PA JOIN APARTEMEN_ROOM AR ON PA.id_kode_room = AR.kode_room where id_transaksi_penginapan = '"+ id_transaksi_penginapan +"' and PA.id_apartemen = AR.id_apartemen")
            data_transaksi = dictfetchall(c)

    print(data_transaksi)
    d0 = date(int(tgl_checkin[0:4]), int(tgl_checkin[5:7]), int(tgl_checkin[8:10]))
    d1 = date(int(tgl_checkout[0:4]), int(tgl_checkout[5:7]), int(tgl_checkout[8:10]))
    delta = d1-d0
    range_tanggal = delta.days
    
    total_harga = []

    for data in data_transaksi:
        total_harga.append(data['harga']*range_tanggal)

    total_pesanan = 0
    for price in total_harga:
        total_pesanan +=price

    # pengguna = request.session['username']
    argument = {
        'nama': nama_penginapan,
        'jenis' : jenis_penginapan,
        'tgl_checkin': tgl_checkin,
        'tgl_checkout': tgl_checkout,
        'jumlah_hari' : range_tanggal,
        'data_transaksi':data_transaksi,
        'total_harga': total_harga,
        'total_pesanan': total_pesanan,
        'total_penginap':total_penginap,
        # 'data_pemesan': data_pemesan,
    }
    
    return render(request,'buatpesanan.html', argument) 

def metodebayar(request):
    # va = request.POST.get('selesaiva', None)
    # print(va)
    return render(request,'metodebayar.html') 

def receipt(request):
    return render(request,'receipt.html') 
