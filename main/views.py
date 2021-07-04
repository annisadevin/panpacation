from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse, Http404

def set_session(request, response):
    response['is_authenticated'] = request.session.get('is_authenticated')
    response['username'] = request.session.get('username')

def main(request):
    response = {}
    set_session(request, response)

    return render(request, 'main/main.html', response)

def filterPencarian(request):
    if (not(request.session.get('is_authenticated'))):
        return redirect('/login/')
    response = {}
    set_session(request, response)

    if (request.method == 'POST'):
        check_in = request.POST.get('check_in')
        check_in = str(check_in) + ' 00:00:00'
        check_out = request.POST.get('check_out')
        check_out = str(check_out) + ' 00:00:00'
        reservasi = request.POST.get('reservasi')
        lokasi = request.POST.get('lokasi')
        jumlah = request.POST.get('jumlah')
        print(check_in)
        print(check_out)
        print(check_out > check_in)

        return redirect('/detail/'+ check_in + '/' + check_out + '/' + reservasi + '/' + lokasi + '/' + jumlah + '/')
    return ('/')

        # if(reservasi == 'Apartemen'):
        #     print("masuk apart")
        #     stmt = '''
        #     SELECT A.id_penginapan
        #     FROM APARTEMEN A, APARTEMEN_ROOM AR, TEMPAT_PENGINAPAN TP
        #     WHERE TP.id_penginapan = A.id_penginapan AND A.id_penginapan = AR.id_apartemen
        #     AND (AR.id_apartemen, AR.kode_room) 
        #     NOT IN 
        #     ((SELECT PAR.id_apartemen, PAR.id_kode_room FROM PILIHAN_APARTEMEN_ROOM PAR, TRANSAKSI_PENGINAPAN TP WHERE PAR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin >= %s) 
        #     INTERSECT 
        #     (SELECT PAR.id_apartemen, PAR.id_kode_room FROM PILIHAN_APARTEMEN_ROOM PAR, TRANSAKSI_PENGINAPAN TP WHERE PAR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkout <= %s))
        #     AND TP.kabkot = %s;
        #     '''
        #     try:
        #         with connection.cursor() as cursor:
        #             cursor.execute(stmt, [check_in, check_out, lokasi])
        #             listTempatPenginapan = cursor.fetchall()
        #         print(listTempatPenginapan)
        #     except:
        #         response['error'] = 'Email atau password salah, silakan coba lagi'

        # elif (reservasi == 'Villa'):
        #     print("masuk villa")
        #     stmt = '''
        #     SELECT V.id_penginapan
        #     FROM VILLA V, TEMPAT_PENGINAPAN TP
        #     WHERE V.id_penginapan = TP.id_penginapan AND V.id_penginapan
        #     NOT IN 
        #     ((SELECT PV.id_villa FROM PILIHAN_VILLA PV, TRANSAKSI_PENGINAPAN TP WHERE PV.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin >= %s) 
        #     INTERSECT 
        #     (SELECT PV.id_villa FROM PILIHAN_VILLA PV, TRANSAKSI_PENGINAPAN TP WHERE PV.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkout <= %s))
        #     AND TP.kabkot = %s;
        #     '''
        #     try:
        #         with connection.cursor() as cursor:
        #             cursor.execute(stmt, [check_in, check_out, lokasi])
        #             listTempatPenginapan = cursor.fetchall()
        # else:
        #     print("masuk kos")
        #     stmt = '''
        #     SELECT K.id_penginapan
        #     FROM KOS K, KOS_ROOM KR, TEMPAT_PENGINAPAN TP
        #     WHERE TP.id_penginapan = K.id_penginapan AND K.id_penginapan = KR.id_kos AND 
        #     (KR.id_kos, KR.kode_room) NOT IN 
        #     ((SELECT PKR.id_kos, PKR.id_kode_room FROM PILIHAN_KOS_ROOM PKR, TRANSAKSI_PENGINAPAN TP WHERE PKR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin >= %s) 
        #     INTERSECT 
        #     (SELECT PKR.id_kos, PKR.id_kode_room FROM PILIHAN_KOS_ROOM PKR, TRANSAKSI_PENGINAPAN TP WHERE PKR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkout <= %s))
        #     AND TP.kabkot = %s;
        #     '''
        #     try:
        #         with connection.cursor() as cursor:
        #             cursor.execute(stmt, [check_in, check_out, lokasi])
        #             listTempatPenginapan = cursor.fetchall()
 
        #     return render(request, 'detail/templates/hasil_pencarian.html', response)

def filterPencarian2(request):
    if (not(request.session.get('is_authenticated'))):
        return redirect('/login/')
    response = {}
    set_session(request, response)

    if (request.method == 'POST'):
        check_in = request.POST.get('check_in')
        check_in = str(check_in) + ' 00:00:00'
        check_out = request.POST.get('check_out')
        check_out = str(check_out) + ' 00:00:00'
        reservasi = request.POST.get('reservasi')
        lokasi = request.POST.get('lokasi')
        jumlah = request.POST.get('jumlah')
        print(check_in)
        print(check_out)
        print(check_out > check_in)

        return redirect('/detail/'+ check_in + '/' + check_out + '/' + reservasi + '/' + lokasi + '/' + jumlah + '/')
    return ('/')

def data_basedOnReservasi(request):
    if request.method == "POST":
        selected_reservasi = request.POST.get("selected_reservasi")
        print(selected_reservasi)
        
        if(selected_reservasi == 'Villa'):
            stmt = '''
            SELECT distinct T.provinsi
            FROM TEMPAT_PENGINAPAN T, VILLA V
            WHERE T.id_penginapan = V.id_penginapan;
            '''
        elif(selected_reservasi == 'Apartemen'):
            stmt = '''
            SELECT distinct T.provinsi
            FROM TEMPAT_PENGINAPAN T, APARTEMEN A
            WHERE T.id_penginapan = A.id_penginapan;
            '''
        else:
            stmt = '''
            SELECT distinct T.provinsi
            FROM TEMPAT_PENGINAPAN T, KOS K
            WHERE T.id_penginapan = K.id_penginapan;
            '''
        
        with connection.cursor() as cursor:
            cursor.execute(stmt)
            listOfKota = cursor.fetchall()

    return JsonResponse({'listKota' : listOfKota})
    
