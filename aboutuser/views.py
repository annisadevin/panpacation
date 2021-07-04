from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse, Http404
from datetime import datetime

def set_session(request, response):
    response['is_authenticated'] = request.session.get('is_authenticated')
    response['username'] = request.session.get('username')
    response['nama_depan'] = request.session.get('nama_depan')
    response['nama_belakang'] = request.session.get('nama_belakang')

def profil(request):
    if (not(request.session.get('is_authenticated'))):
        return redirect('/login/')
    response = {}
    set_session(request, response)

    stmt1 = '''
    SELECT distinct T.id_transaksi, T.total_bayar, TP.tgl_checkin, TP.tgl_checkout, TE.nama, TE.provinsi, F.link
    FROM TRANSAKSI T, TRANSAKSI_PENGINAPAN TP, PILIHAN_KOS_ROOM PKR, KOS_ROOM KR, KOS K, TEMPAT_PENGINAPAN TE, FOTO F
    WHERE T.pengguna = %s AND T.id_transaksi = TP.id_transaksi AND TP.id_transaksi_penginapan = PKR.id_transaksi_penginapan AND PKR.id_kos = KR.id_kos AND KR.id_kos = K.id_penginapan AND K.id_penginapan = TE.id_penginapan AND TE.id_penginapan = F.id_penginapan;
    '''

    stmt2 = '''
    SELECT distinct T.id_transaksi, T.total_bayar, TP.tgl_checkin, TP.tgl_checkout, TE.nama, TE.provinsi, F.link
    FROM TRANSAKSI T, TRANSAKSI_PENGINAPAN TP, PILIHAN_APARTEMEN_ROOM PAR, APARTEMEN_ROOM AR, APARTEMEN A, TEMPAT_PENGINAPAN TE, FOTO F
    WHERE T.pengguna = %s AND T.id_transaksi = TP.id_transaksi AND TP.id_transaksi_penginapan = PAR.id_transaksi_penginapan AND PAR.id_apartemen = AR.id_apartemen AND AR.id_apartemen = A.id_penginapan AND A.id_penginapan = TE.id_penginapan AND TE.id_penginapan = F.id_penginapan;
    '''

    stmt3 = '''
    SELECT distinct T.id_transaksi, T.total_bayar, TP.tgl_checkin, TP.tgl_checkout, TE.nama, TE.provinsi, F.link
    FROM TRANSAKSI T, TRANSAKSI_PENGINAPAN TP, PILIHAN_VILLA PV, VILLA V, TEMPAT_PENGINAPAN TE, FOTO F
    WHERE T.pengguna = %s AND T.id_transaksi = TP.id_transaksi AND TP.id_transaksi_penginapan = PV.id_transaksi_penginapan AND PV.id_villa = V.id_penginapan AND V.id_penginapan = TE.id_penginapan AND TE.id_penginapan = F.id_penginapan;
    '''
    try:
        with connection.cursor() as cursor:
            cursor.execute(stmt1, [request.session.get('username')])
            listTransaksiKos = cursor.fetchall()
        with connection.cursor() as cursor:
            cursor.execute(stmt2, [request.session.get('username')])
            listTransaksiApart = cursor.fetchall() 
        with connection.cursor() as cursor:
            cursor.execute(stmt3, [request.session.get('username')])
            listTransaksiVilla = cursor.fetchall()
        response['listTransaksi'] = listTransaksiKos + listTransaksiApart + listTransaksiVilla
    except:
        response['error'] = 'ada suatu kesalahan'

    return render(request, 'aboutuser/profil.html', response)

def review(request, idtransaksi):
    if (not(request.session.get('is_authenticated'))):
        return redirect('/login/')
    response = {}
    set_session(request, response)

    if request.method == "POST":
        print("masuk post")
        stmt1 = '''
        SELECT TP.id_transaksi_penginapan FROM TRANSAKSI_PENGINAPAN TP, TRANSAKSI T WHERE T.id_transaksi = TP.id_transaksi AND T.id_transaksi = %s;
        '''
        
        with connection.cursor() as cursor:
            cursor.execute(stmt1, [idtransaksi])
            idTransaksiPenginapan = cursor.fetchall()
        idTransaksiPenginapan = idTransaksiPenginapan[0][0]
        print(idTransaksiPenginapan)

        stmt2 = '''
        INSERT INTO REVIEW (pengguna, waktu, id_transaksi_penginapan, isi, rating)
        VALUES (%s,%s,%s,%s,%s);
        '''

        try:
            pengguna = request.session.get('username')
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            waktu = dt_string
            isi = request.POST.get('reviewIsi')
            rating = request.POST.get('rating')
            print(pengguna)
            print(waktu)
            print(isi)
            print(rating)
            with connection.cursor() as cursor:
                cursor.execute(stmt2, [pengguna, waktu, idTransaksiPenginapan, isi, rating])
                connection.commit()
            return redirect('/profil/')
        except:
            response['error'] = 'ada suatu kesalahan'
    
    return redirect('/profil/')

def dataMyReview(request):
    if (not(request.session.get('is_authenticated'))):
        return redirect('/login/')
    response = {}
    set_session(request, response)

    if request.method == "POST":
        id_transaksi = request.POST.get("id_transaksi")

        stmt1 = '''
        SELECT TP.id_transaksi_penginapan FROM TRANSAKSI_PENGINAPAN TP, TRANSAKSI T WHERE T.id_transaksi = TP.id_transaksi AND T.id_transaksi = %s;
        '''
        
        with connection.cursor() as cursor:
            cursor.execute(stmt1, [id_transaksi])
            idTransaksiPenginapan = cursor.fetchall()
        idTransaksiPenginapan = idTransaksiPenginapan[0][0]
        print(idTransaksiPenginapan)
    
        stmt2 = '''
        SELECT R.isi, R.rating FROM REVIEW R WHERE R.pengguna = %s AND R.id_transaksi_penginapan = %s;
        '''
        try:
            pengguna = request.session.get('username')
            with connection.cursor() as cursor:
                cursor.execute(stmt2, [pengguna, idTransaksiPenginapan])
                myreview = cursor.fetchall()
            print(myreview)
            return JsonResponse({"listMyReview" : myreview})
        except:
            response['error'] = 'ada suatu kesalahan'

    return redirect('/profil/')
