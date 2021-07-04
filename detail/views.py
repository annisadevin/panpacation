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
        #Filter berdasarkan lokasi
        selectedLokasi = request.POST.get('lokasi')
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'Apartemen':
                if selectedLokasi == 'jabodetabek':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'A%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')")
                    res = dictfetchall(c)
                    context['res'] = res 
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'A%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')) AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 

            #Villa
            elif reservasi == 'Villa':
                if selectedLokasi == 'jabodetabek':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'V%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')")
                    res = dictfetchall(c)
                    context['res'] = res 
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'V%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')) AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'Kos':
                if selectedLokasi == 'jabodetabek':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'K%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')")
                    res = dictfetchall(c)
                    context['res'] = res 
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'K%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')) AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif selectedLokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif selectedLokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif selectedLokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif selectedLokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                


        #Filter berdasarkan rating
        rating = request.POST.get('bintang')
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'Apartemen':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Villa
            elif reservasi == 'Villa':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'Kos':
                if rating == '5':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=5 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '4':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=4 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '3':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=3 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '2':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=2 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif rating == '1':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.rating=1 AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml
                



        #Filter berdasarkan price
        priceMin = request.POST.get('priceMin')
        priceMax = request.POST.get('priceMax')
       
        if priceMin != "" and priceMax != "":
            with connection.cursor() as c:
                if reservasi == 'Apartemen':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan LIKE 'A%'", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan LIKE 'A%') AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'Villa':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan LIKE 'V%'", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan LIKE 'V%') AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif reservasi == 'Kos':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan LIKE 'K%'", [priceMin, priceMax])
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.harga_termurah >= %s AND tp.harga_termurah <= %s AND tp.id_penginapan LIKE 'K%') AS temp", [priceMin, priceMax])
                    jml = dictfetchall(c)
                    context['jumlah'] = jml






        #Filter berdasarkan checkin dan checkout
        inputCheckin = request.POST.get('checkin')
        inputCheckout = request.POST.get('checkout')



    elif request.method == "GET":

         #Filter berdasarkan lokasi
        with connection.cursor() as c:
            #Apartemen
            if reservasi == 'Apartemen':
                if lokasi == 'jabodetabek':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'A%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')")
                    res = dictfetchall(c)
                    context['res'] = res 
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'A%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')) AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif lokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif lokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'A%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 

            #Villa
            elif reservasi == 'Villa':
                if lokasi == 'jabodetabek':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'V%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')")
                    res = dictfetchall(c)
                    context['res'] = res 
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'V%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')) AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif lokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif lokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'V%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

            #Kos
            elif reservasi == 'Kos':
                if lokasi == 'jabodetabek':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'K%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')")
                    res = dictfetchall(c)
                    context['res'] = res 
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.id_penginapan LIKE 'K%' AND tp.provinsi='DKI Jakarta' OR kabkot IN ('Bogor', 'Depok', 'Tangerang', 'Tangerang Selatan', 'Bekasi')) AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  
            
                elif lokasi == 'jawaBarat':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Barat' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'jawaTengah':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Tengah' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml  

                elif lokasi == 'jawaTimur':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur'AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Jawa Timur' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'banten':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Banten' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml 
                
                elif lokasi == 'yogyakarta':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Yogyakarta' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml

                elif lokasi == 'bali':
                    c.execute("SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%'")
                    res = dictfetchall(c)
                    context['res'] = res
                    c.execute("SELECT COUNT(*) FROM(SELECT distinct on (nama) nama, link, alamat_lengkap, rating, harga_termurah FROM tempat_penginapan tp, foto f WHERE tp.Id_penginapan = f.Id_penginapan AND tp.provinsi='Bali' AND tp.id_penginapan LIKE 'K%') AS temp")
                    jml = dictfetchall(c)
                    context['jumlah'] = jml
     

        return render(request,'hasil_pencarian.html', context) 

    

def hasil_pencarian2(request, reservasi):
    context = {}

    return render(request,'hasil_pencarian.html', context) 




