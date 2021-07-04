from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, DataError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple
from django.http import JsonResponse
from datetime import datetime


def detailpencarian(request, id, checkin, checkout, jml):
    username = request.session.get('username')
    iddddd = id
    jenis = ''
    if(id[0] == 'A'):
        jenis = 'Apartemen'
    elif(id[0] == 'V'):
        jenis = 'Villa'
    else:
        jenis = 'Kos'
    a=0
    cvd=''
    cvdstarter=0


    with connection.cursor() as c:
        c.execute("SELECT nama, iswifi, isparkirluas, no_telp, rating, alamat_lengkap, alamat_link FROM tempat_penginapan WHERE id_penginapan=%s", [id])
        res = dictfetchall(c)
    
        c.execute("SELECT Link FROM Foto WHERE id_penginapan=%s", [id])
        rep = dictfetchall(c)

        c.execute("SELECT * FROM DATA_DETAIL2 WHERE id_kos = %s",[id])
        hotel = dictfetchall(c)

        c.execute("SELECT * FROM DATA_DETAIL WHERE id_apartemen = %s",[id])
        apart = dictfetchall(c)

        c.execute("select * from transaksi ORDER BY id_transaksi DESC limit 1")
        transaksi = dictfetchall(c)

        c.execute("select * from transaksi_penginapan ORDER BY id_transaksi DESC limit 1")
        transaksi_penginapan = dictfetchall(c)

        c.execute("select * from review;")
        rating = dictfetchall(c)

    arrstatus = []
    status = 1
    tmp ={}

    halo = None

    if jenis == 'Apartemen':
        halo = apart
    else:
        halo = hotel    
    for i in halo:
        tmp = i
        tmp["status"] =status
        status = status + 1
        arrstatus.append(tmp.copy())

    kapasitas=[]
    asik = len(arrstatus)+1
    for i in range(asik):
        hali = "'"+str(i)+"'"
        a = request.POST.get(str(i), None)
        if(a== None):
            kapasitas = kapasitas
        else:
            kapasitas.append(a)
        
    a = int(res[0]['iswifi']) + int(res[0]['isparkirluas'])
    link = rep[0]
    arrlink = rep[1:]
    jumlahfoto= len(rep)
    
    if(checkin == None and checkout== None and jml == None):
        response = {
            'kode':id,
            'namahotel':res[0]['nama'],
            'alamat':res[0]['alamat_lengkap'],
            'notelp':res[0]['no_telp'],
            'wifi':res[0]['iswifi'],
            'parkir':res[0]['isparkirluas'],
            'totalnya':a,
            'linknya':res[0]['alamat_link'],
            'rating':res[0]['rating'],
            'foto':rep,
            'foto1':link,
            'foto2':arrlink,
            'jenis':jenis,
            'jmlfoto':jumlahfoto,
            'cvd':cvd,
            'cvdstarter': cvdstarter,
            'room' : arrstatus,
            'rating' : rating,
        }
    else:
        response = {
            'kode':id,
            'checkin':checkin,
            'checkout':checkout,
            'jml':jml,
            'namahotel':res[0]['nama'],
            'alamat':res[0]['alamat_lengkap'],
            'notelp':res[0]['no_telp'],
            'wifi':res[0]['iswifi'],
            'parkir':res[0]['isparkirluas'],
            'totalnya':a,
            'linknya':res[0]['alamat_link'],
            'rating':res[0]['rating'],
            'foto':rep,
            'foto1':link,
            'foto2':arrlink,
            'jenis':jenis,
            'jmlfoto':jumlahfoto,
            'cvd':cvd,
            'cvdstarter': cvdstarter,
            'room' : arrstatus,
            'rating' : rating,
        }

    if (len(transaksi)!=0):
        last_id = transaksi[0]['id_transaksi']
        last_two_digit = last_id[2:]
        id = int(last_two_digit) + 1
        newest_digit= '{:08d}'.format(id)
        newest_id = 'TR'+newest_digit
    else:
        newest_id = 'TR00000001'

    if (len(transaksi_penginapan)!=0):
        last_id = transaksi_penginapan[0]['id_transaksi_penginapan']
        last_two_digit = last_id[2:]
        id = int(last_two_digit) + 1
        newest_digit= '{:08d}'.format(id)
        newest_idtp = 'TP'+newest_digit
    else:
        newest_idtp = 'TP00000001'

    if request.method == 'POST':
        ci = request.POST.get('checkin', None)
        co = request.POST.get('checkout', None)
        j = request.POST.get('jml', None)
        now = datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            if (ci > co):
                return redirect('/')

            with connection.cursor() as c:
                c.execute("INSERT INTO transaksi VALUES (%s, %s, %s, %s, %s, %s)", [newest_id,'Belum bayar',0, 'VA', username, time])
                c.execute("INSERT INTO transaksi_penginapan VALUES (%s, %s, %s, %s, %s)", [newest_idtp, newest_id,ci, co, 0])
                if(jenis == 'Apartemen'):
                    for i in range(len(kapasitas)):
                        c.execute("INSERT INTO pilihan_apartemen_room VALUES(%s, %s, %s)", [newest_idtp, iddddd, kapasitas[i]])
                elif(jenis == "Kos"):
                    for i in range(len(kapasitas)):
                        c.execute("INSERT INTO pilihan_kos_room VALUES(%s, %s, %s)", [newest_idtp, iddddd, kapasitas[i]])
                else:
                    c.execute("INSERT INTO pilihan_villa VALUES(%s, %s)", [newest_idtp, iddddd])
                
            return redirect('/detail/')

        except IntegrityError:
            messages.error(request, 'Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    


    return render(request,'detail_pencarian.html', response) 

def getkodefromcheckin(request, id, checkin, checkout, jml):
    with connection.cursor() as c:
        if(id[0] == 'A'):
            c.execute("SELECT * FROM DATA_DETAIL WHERE id_apartemen = %s ",[id])
        if(id[0] == 'K'):
            c.execute("SELECT * FROM data_detail2 WHERE Id_Kos=%s",[id])
        res = dictfetchall(c)

        
    arr = []
    status = 1
    tmp ={}
    for i in res:
        tmp = i
        tmp["status"] =status
        status = status + 1
        arr.append(tmp.copy())

    return JsonResponse(arr, safe = False) 



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]