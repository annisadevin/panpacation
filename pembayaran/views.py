from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db import connection
from django.db.utils import InternalError, IntegrityError
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple

# Create your views here.

def buatpesanan(request):
    namap = request.POST.get('namapemesan', None)
    jenis = request.POST.get('jenistest', None)
    print(namap)
    return render(request,'buatpesanan.html') 

def metodebayar(request):
    # va = request.POST.get('selesaiva', None)
    # print(va)
    return render(request,'metodebayar.html') 

def receipt(request):
    return render(request,'receipt.html') 

