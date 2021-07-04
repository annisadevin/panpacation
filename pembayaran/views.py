from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple

from datetime import date

def set_session(request, response):
    response['is_authenticated'] = request.session.get('is_authenticated')
    response['username'] = request.session.get('username')
    response['nama_depan'] = request.session.get('nama_depan')
    response['nama_belakang'] = request.session.get('nama_belakang')

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

# views untuk fitur buat pesanan

def buatpesanan(request, id_penginapan, tgl_checkin, tgl_checkout, total_penginap):
    username = request.session.get('username')
    no_id = request.session.get('no_id')

    nama_depan = request.session.get('nama_depan')
    nama_belakang = request.session.get('nama_belakang')
    with connection.cursor() as c:
        c.execute("SELECT no_telp FROM PENGGUNA where username = '"+ username +"'")
        res = dictfetchall(c)
    no_telp = res[0]['no_telp']
    nama_pemesan = nama_depan + '' +nama_belakang
    
    with connection.cursor() as c:
        c.execute("SELECT * FROM PENGGUNA where username = '"+ username +"'")
        res = dictfetchall(c)

    data_pemesan = res[0]

    with connection.cursor() as c:
        c.execute("SELECT * FROM TANGGUNGAN where username_pengguna = '"+ username +"'")
        tanggungan = dictfetchall(c)

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
    init = 1
    list_penginap = []

    for i in range(total_penginap):
        list_penginap.append(str(init))
        init+=1
    
    if request.method == "POST": 
        with connection.cursor() as c:
            c.execute("UPDATE TRANSAKSI_PENGINAPAN set TOTAL_HARGA=%s", [total_pesanan])
        
        counter = 0

        test_terpilih = request.POST.get("test-terpilih")

        for i in range(len(tanggungan)):
            stringsss = 'testcovid'+str(i)
            if request.POST.get(stringsss)=='satu':
                counter +=1

        harga_test_covid = int(test_terpilih)*counter
        total_semua = harga_test_covid + total_pesanan

        with connection.cursor() as c:
            c.execute("update transaksi set total_bayar=%s", [total_semua])

        with connection.cursor() as c:
            c.execute("update transaksi_penginapan set total_harga=%s", [total_pesanan])

        with connection.cursor() as c:
            c.execute("update transaksi_test_covid set total_harga=%s", [harga_test_covid])
        return metodebayar(request, nama_pemesan, id_penginapan, nama_penginapan, tgl_checkin, tgl_checkout, range_tanggal, total_pesanan, harga_test_covid, total_semua, no_telp,  total_penginap)
   
        # return redirect("/pembayaran/metodebayar/" + nama_pemesan + "/" + id_penginapan + "/" +  nama_penginapan + "/" +  tgl_checkin +"/" + tgl_checkout +"/" + str(range_tanggal) +"/" + str(total_pesanan)+"/" +str(harga_test_covid)+"/" +str(total_semua)+"/" +no_telp+"/" + str(total_penginap) + "/")
        
    if request.is_ajax:
        if request.method == "POST": 
            nama = request.POST.get("nama_modal")
            id = request.POST.get("id_modal")

            with connection.cursor() as c:
                c.execute("INSERT INTO TANGGUNGAN VALUES('"+ username +"','"+ id +"','"+ nama +"', NULL)")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    with connection.cursor() as c:
        c.execute("SELECT * FROM TEST_COVID_AVAIL")
        test_covid_avail = dictfetchall(c)
        
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
        'data_pemesan': data_pemesan,
        'list_penginap':list_penginap,
        'tanggungan':tanggungan,
        'test_covid_avail':test_covid_avail,
    }
    set_session(request, argument)
    return render(request,'buatpesanan.html', argument) 

def metodebayar(request, nama_pemesan, id_penginapan, nama_penginapan, tgl_checkin, tgl_checkout, durasi, total_harga_penginapan, total_test_covid, total_semua, no_telp, total_penginap):
    response = {} 
    set_session(request, response)
    if request.method == "POST": 
        return receipt(request, nama_pemesan, id_penginapan, nama_penginapan, tgl_checkin, tgl_checkout, durasi, total_harga_penginapan, total_test_covid, total_semua, no_telp, total_penginap)

        # return redirect("/pembayaran/receipt/" + nama_pemesan + "/" + id_penginapan + "/" +  nama_penginapan + "/" +  tgl_checkin +"/" + tgl_checkout +"/" + str(durasi) +"/" + str(total_pesanan)+"/" +str(harga_test_covid)+"/" +str(total_semua)+"/" +no_telp+"/" + str(total_penginap) + "/")

    argument = {
        'nama_pemesan':nama_pemesan,
        'nama_penginapan':nama_penginapan,
        'tgl_checkin':tgl_checkin,
        'tgl_checkout':tgl_checkout,
        'durasi':durasi,
        'total_harga_penginapan':total_harga_penginapan,
        'total_test_covid': total_test_covid,
        'total_semua':total_semua,
        'no_telp': no_telp,
        'id_penginapan': id_penginapan,
        'total_penginap': total_penginap,
    }
    set_session(request, argument)
    return render(request,'metodebayar.html', argument) 

def receipt(request, nama_pemesan, id_penginapan, nama_penginapan, tgl_checkin, tgl_checkout, durasi, total_harga_penginapan, total_test_covid, total_semua, no_telp, total_penginap):
     
    
    argument = {
        'nama_pemesan':nama_pemesan,
        'nama_penginapan':nama_penginapan,
        'tgl_checkin':tgl_checkin,
        'tgl_checkout':tgl_checkout,
        'durasi':durasi,
        'total_harga_penginapan':total_harga_penginapan,
        'total_test_covid': total_test_covid,
        'total_semua':total_semua,
        'no_telp': no_telp,
        'id_penginapan': id_penginapan,
        'total_penginap': total_penginap,
    }
    set_session(request, argument)
    return render(request,'receipt.html', argument) 
