from django.urls import path
from pembayaran.views import *

app_name = 'pembayaran'
urlpatterns = [
    path('buatpesanan/', buatpesanan, name='buatpesanan'),
    path('metodebayar/', metodebayar, name='metodebayar'),
    path('receipt/', receipt, name='receipt'),

]

