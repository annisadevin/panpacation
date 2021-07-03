from django.shortcuts import render


def feeds(request):
    return render(request, 'feeds/feeds.html')

