# Create your views here.

from django.shortcuts import render


def profil(request):
    return render(request, 'aboutuser/profil.html')