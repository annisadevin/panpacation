from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse, Http404

def set_session(request, response):
    response['is_authenticated'] = request.session.get('is_authenticated')
    response['username'] = request.session.get('username')
    response['nama_depan'] = request.session.get('nama_depan')
    response['nama_belakang'] = request.session.get('nama_belakang')

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

        if (check_in > check_out):
            return redirect('/')
        print(check_in)
        print(check_out)
        print(check_out > check_in)
        print(lokasi)

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
        print(listOfKota)

    return JsonResponse({'listKota' : listOfKota})

def random(request):
    if (not(request.session.get('is_authenticated'))):
        return redirect('/login/')
    response = {}
    set_session(request, response)
    return render(request, 'main/randomDesti.html', response)
    