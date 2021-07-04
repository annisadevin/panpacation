from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse, Http404

def set_session(request, response):
    response['is_authenticated'] = request.session.get('is_authenticated')
    response['username'] = request.session.get('username')
    response['nama_depan'] = request.session.get('nama_depan')
    response['nama_belakang'] = request.session.get('nama_belakang')

def profil(request):
    response = {}
    set_session(request, response)

    stmt = '''
    SELECT TP.id_transaksi_penginapan
    FROM TRANSAKSI_PENGINAPAN TP, TRANSAKSI T, PENGGUNA P
    WHERE TP.id_transaksi = T.id_transaksi AND T.pengguna = P.username AND P.username = %s;
    '''
    try:
        with connection.cursor() as cursor:
            cursor.execute(stmt, [request.session.get('username')])
            listTransaksi = cursor.fetchall()
        response['listTransaksi'] = listTransaksi
    except:
        response['error'] = 'Email atau password salah, silakan coba lagi'

    return render(request, 'aboutuser/profil.html', response)