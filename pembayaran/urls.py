from django.urls import path
from pembayaran.views import *

app_name = 'pembayaran'
urlpatterns = [
    path('buatpesanan/<str:id_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<int:total_penginap>/', buatpesanan, name='buatpesanan'),
    path('metodebayar/', metodebayar, name='metodebayar'),
    path('receipt/', receipt, name='receipt'),
]


