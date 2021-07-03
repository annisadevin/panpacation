from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple

def detail_pencarian(request):
    namap = request.POST.get('checkin', None)
    print(namap)
    return render(request,'detail_pencarian.html') 
