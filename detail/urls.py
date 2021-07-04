from django.urls import path
from detail.views import *
from detail.views2 import *

app_name = 'detail'
urlpatterns = [
    path('<str:checkin>/<str:checkout>/<str:reservasi>/<str:lokasi>/<str:jumlah>/', hasil_pencarian, name='hasil_pencarian'),
    path('<str:reservasi>', hasil_pencarian2, name='hasil_pencarian2' ),
    path('detail_pencarian/', detail_pencarian, name='detail_pencarian'),
]

