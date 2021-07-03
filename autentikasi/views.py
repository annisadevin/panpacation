from django.shortcuts import render


def register(request):
    return render(request, 'autentikasi/register.html')

def login(request):
    return render(request, 'autentikasi/login.html')