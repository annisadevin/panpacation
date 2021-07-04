from django.shortcuts import render, redirect
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse, Http404

def set_session(request, response):
    response['is_authenticated'] = request.session.get('is_authenticated')
    response['username'] = request.session.get('username')
    response['nama_depan'] = request.session.get('nama_depan')
    response['nama_belakang'] = request.session.get('nama_belakang')

def register(request):
    if (request.session.get('is_authenticated')):
        return redirect('/')
    response = {}

    if (request.method == 'POST'):
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        email = request.POST.get('email')
        password = request.POST.get('password')

        stmt1 = '''
        INSERT INTO pengguna(username, password, nama_depan, nama_belakang) VALUES (%s,%s,%s,%s);
        '''

        try:
            with connection.cursor() as cursor:
                cursor.execute(stmt1, [email, password, nama_depan, nama_belakang])
                connection.commit()
            
            request.session['username'] = request.POST.get('email')
            request.session['nama_depan'] = nama_depan
            request.session['nama_belakang'] = nama_belakang
            request.session['is_authenticated'] = True
            return redirect('/')
        except Exception as e:
            e = str(e)
            if ('already exists' in e):
                response['error'] = 'Email telah digunakan, silakan gunakan email lain'
            else:
                response['error'] = 'Ada suatu kesalahan'

    return render(request, 'autentikasi/register.html', response)

def login(request):
    if (request.session.get('is_authenticated')):
        return redirect('/')
    response = {}

    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)

        stmt = '''
        SELECT * FROM pengguna WHERE username=%s AND PASSWORD=%s;
        '''
        try:
            user = tuple()
            with connection.cursor() as cursor:
                cursor.execute(stmt, [email, password])
                user = cursor.fetchone()
            request.session['username'] = user[0]
            request.session['nama_depan'] = user[2]
            request.session['nama_belakang'] = user[3]
            request.session['is_authenticated'] = True
            return redirect('/')
        except:
            response['error'] = 'Email atau password salah, silakan coba lagi'

    return render(request, 'autentikasi/login.html', response)

def logout(request):
    request.session.flush()
    return redirect('/')




    