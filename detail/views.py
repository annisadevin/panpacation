from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple

# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def hasil_pencarian(request, checkin, checkout, reservasi, lokasi, jumlah):
    context = {}

    # with connection.cursor() as c:
    #     c.execute("SELECT * FROM PENGGUNA")
    #     res = dictfetchall(c)

    # print(res[0]['username'])

    # namap = request.POST.get('checkin', None)
   



    # if request.method == "POST":
    #     filter = []
    #     kota = request.POST.get('pilihKota')
    #     # rating = request.POST.get('bintang')
    #     filter.append(kota)
       


    if request.method == "POST":
        print("masuk POST")
        #Filter berdasarkan lokasi
        selectedLokasi = request.POST.get('lokasi')
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'Apartemen':
                if selectedLokasi == 'dkiJakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 

            #Villa
            elif reservasi == 'Villa':
                if selectedLokasi == 'dkiJakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'Kost':
                if selectedLokasi == 'dkiJakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                


        #Filter berdasarkan rating
        rating = request.POST.get('bintang')
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'Apartemen':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Villa
            elif reservasi == 'Villa':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'Kost':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml
                



        #Filter berdasarkan price
        priceMin = request.POST.get('priceMin')
        priceMax = request.POST.get('priceMax')
       
        if priceMin != "" and priceMax != "":
            with connection.cursor() as c:
                if reservasi == 'Apartemen':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from apartemen)", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from apartemen)) AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'Villa':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from villa)", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from villa)) AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'Kost':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from kos)", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from kos)) AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml


        #Filter berdasarkan checkin dan checkout
        inputCheckin = request.POST.get('checkin')
        inputCheckout = request.POST.get('checkout')

        with connection.cursor() as c:
                if reservasi == 'Apartemen':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM APARTEMEN A, APARTEMEN_ROOM AR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = A.id_penginapan AND A.id_penginapan = AR.id_apartemen AND TEM.id_penginapan = F.id_penginapan AND (AR.id_apartemen, AR.kode_room) NOT IN (SELECT PAR.id_apartemen, PAR.id_kode_room FROM PILIHAN_APARTEMEN_ROOM PAR, TRANSAKSI_PENGINAPAN TP WHERE PAR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)",[inputCheckin, inputCheckout])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM APARTEMEN A, APARTEMEN_ROOM AR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = A.id_penginapan AND A.id_penginapan = AR.id_apartemen AND TEM.id_penginapan = F.id_penginapan AND (AR.id_apartemen, AR.kode_room) NOT IN (SELECT PAR.id_apartemen, PAR.id_kode_room FROM PILIHAN_APARTEMEN_ROOM PAR, TRANSAKSI_PENGINAPAN TP WHERE PAR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)) AS temp", [inputCheckin, inputCheckout])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'Villa':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM VILLA V, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = V.id_penginapan AND TEM.id_penginapan = F.id_penginapan AND V.id_penginapan NOT IN (SELECT PV.id_villa FROM PILIHAN_VILLA PV, TRANSAKSI_PENGINAPAN TP WHERE PV.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)",[inputCheckin, inputCheckout])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM VILLA V, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = V.id_penginapan AND TEM.id_penginapan = F.id_penginapan AND V.id_penginapan NOT IN (SELECT PV.id_villa FROM PILIHAN_VILLA PV, TRANSAKSI_PENGINAPAN TP WHERE PV.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)) AS temp", [inputCheckin, inputCheckout])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'Kost':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM KOS K, KOS_ROOM KR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = K.id_penginapan AND K.id_penginapan = KR.id_kos AND TEM.id_penginapan = F.id_penginapan AND (KR.id_kos, KR.kode_room) NOT IN (SELECT PKR.id_kos, PKR.id_kode_room FROM PILIHAN_KOS_ROOM PKR, TRANSAKSI_PENGINAPAN TP WHERE PKR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)",[inputCheckin, inputCheckout])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM KOS K, KOS_ROOM KR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = K.id_penginapan AND K.id_penginapan = KR.id_kos AND TEM.id_penginapan = F.id_penginapan AND (KR.id_kos, KR.kode_room) NOT IN (SELECT PKR.id_kos, PKR.id_kode_room FROM PILIHAN_KOS_ROOM PKR, TRANSAKSI_PENGINAPAN TP WHERE PKR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)) AS temp", [inputCheckin, inputCheckout])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml



        context['ci'] = checkin
        context['co'] = checkout
        context['jum'] = jumlah

        return render(request,'hasil_pencarian.html', context) 












































    elif request.method == "GET":
        print("masuk GET")
        print(lokasi)

        #Berdasarkan lokasi
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'Apartemen':
                if lokasi == 'DKI Jakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif lokasi == 'Jawa Barat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'Jawa Tengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'Jawa Timur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'Banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'Yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif lokasi == 'Bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 

            #Villa
            elif reservasi == 'Villa':
                if lokasi == 'DKI Jakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif lokasi == 'Jawa Barat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'Jawa Tengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'Jawa Timur':
                    print("berhasillllllllll")
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'Banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'Yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif lokasi == 'Bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'Kost':
                if lokasi == 'DKI Jakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml   
            
                elif lokasi == 'Jawa Barat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'Jawa Tengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'Jawa Timur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'Banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'Yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif lokasi == 'Bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml
     
        context['ci'] = checkin
        context['co'] = checkout
        context['jum'] = jumlah

        return render(request,'hasil_pencarian.html', context) 
   

    






















def hasil_pencarian2(request, reservasi):
    context = {}

    if request.method == "GET":
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'apartemen':
                c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'A%'")
                res = dictfetchall(c)
                context['res'] = res
                c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'A%') AS temp")
                jml = dictfetchall(c)
                context['jumlah'] = jml

            #Villa
            elif reservasi == 'villa':
                c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'V%'")
                res = dictfetchall(c)
                context['res'] = res
                c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'V%') AS temp")
                jml = dictfetchall(c)
                context['jumlah'] = jml

            #Kost
            elif reservasi == 'kost':
                c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'K%'")
                res = dictfetchall(c)
                context['res'] = res
                c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'K%') AS temp")
                jml = dictfetchall(c)
                context['jumlah'] = jml

        context['ci'] = None
        context['co'] = None
        context['jum'] = None

        return render(request,'hasil_pencarian.html', context) 

    



























    elif request.method == "POST":
        #Filter berdasarkan lokasi
        selectedLokasi = request.POST.get('lokasi')
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'apartemen':
                if selectedLokasi == 'dkiJakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 

            #Villa
            elif reservasi == 'villa':
                if selectedLokasi == 'dkiJakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'kost':
                if selectedLokasi == 'dkiJakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='DKI Jakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                


        #Filter berdasarkan rating
        rating = request.POST.get('bintang')
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'apartemen':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Villa
            elif reservasi == 'villa':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'kost':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml
                



        #Filter berdasarkan price
        priceMin = request.POST.get('priceMin')
        priceMax = request.POST.get('priceMax')
       
        if priceMin != "" and priceMax != "":
            with connection.cursor() as c:
                if reservasi == 'apartemen':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from apartemen)", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from apartemen)) AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'villa':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from villa)", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from villa)) AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'kost':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from kos)", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan IN (select id_penginapan from kos)) AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml






        #Filter berdasarkan checkin dan checkout
        inputCheckin = request.POST.get('checkin')
        inputCheckout = request.POST.get('checkout')

        with connection.cursor() as c:
                if reservasi == 'apartemen':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM APARTEMEN A, APARTEMEN_ROOM AR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = A.id_penginapan AND A.id_penginapan = AR.id_apartemen AND TEM.id_penginapan = F.id_penginapan AND (AR.id_apartemen, AR.kode_room) NOT IN (SELECT PAR.id_apartemen, PAR.id_kode_room FROM PILIHAN_APARTEMEN_ROOM PAR, TRANSAKSI_PENGINAPAN TP WHERE PAR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)",[inputCheckin, inputCheckout])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM APARTEMEN A, APARTEMEN_ROOM AR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = A.id_penginapan AND A.id_penginapan = AR.id_apartemen AND TEM.id_penginapan = F.id_penginapan AND (AR.id_apartemen, AR.kode_room) NOT IN (SELECT PAR.id_apartemen, PAR.id_kode_room FROM PILIHAN_APARTEMEN_ROOM PAR, TRANSAKSI_PENGINAPAN TP WHERE PAR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)) AS temp", [inputCheckin, inputCheckout])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'villa':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM VILLA V, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = V.id_penginapan AND TEM.id_penginapan = F.id_penginapan AND V.id_penginapan NOT IN (SELECT PV.id_villa FROM PILIHAN_VILLA PV, TRANSAKSI_PENGINAPAN TP WHERE PV.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)",[inputCheckin, inputCheckout])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM VILLA V, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = V.id_penginapan AND TEM.id_penginapan = F.id_penginapan AND V.id_penginapan NOT IN (SELECT PV.id_villa FROM PILIHAN_VILLA PV, TRANSAKSI_PENGINAPAN TP WHERE PV.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)) AS temp", [inputCheckin, inputCheckout])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'kost':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM KOS K, KOS_ROOM KR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = K.id_penginapan AND K.id_penginapan = KR.id_kos AND TEM.id_penginapan = F.id_penginapan AND (KR.id_kos, KR.kode_room) NOT IN (SELECT PKR.id_kos, PKR.id_kode_room FROM PILIHAN_KOS_ROOM PKR, TRANSAKSI_PENGINAPAN TP WHERE PKR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)",[inputCheckin, inputCheckout])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah, tp.id_penginapan FROM KOS K, KOS_ROOM KR, TEMPAT_PENGINAPAN TEM, FOTO F WHERE TEM.id_penginapan = K.id_penginapan AND K.id_penginapan = KR.id_kos AND TEM.id_penginapan = F.id_penginapan AND (KR.id_kos, KR.kode_room) NOT IN (SELECT PKR.id_kos, PKR.id_kode_room FROM PILIHAN_KOS_ROOM PKR, TRANSAKSI_PENGINAPAN TP WHERE PKR.id_transaksi_penginapan = TP.id_transaksi_penginapan AND TP.tgl_checkin <= %s AND TP.tgl_checkout >= %s)) AS temp", [inputCheckin, inputCheckout])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml


        context['ci'] = None
        context['co'] = None
        context['jum'] = None

        return render(request,'hasil_pencarian.html', context)

