from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple

# Create your views here.

def hasil_pencarian(request):
    with connection.cursor() as c:
        c.execute("SELECT * FROM PENGGUNA")
        res = dictfetchall(c)


    # namap = request.POST.get('checkin', None)
    print(res[0]['username'])
    return render(request,'hasil_pencarian.html') 

    

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



