from django.urls import path
from pembayaran.views import *

app_name = 'pembayaran'
urlpatterns = [
    path('buatpesanan/<str:id_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<int:total_penginap>/', buatpesanan, name='buatpesanan'),
    path('metodebayar/<str:nama_pemesan>/<str:nama_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<int:durasi>/<int:total_harga_penginapan>', metodebayar, name='metodebayar'),
    path('receipt/<str:nama_pemesan>/<str:nama_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<int:durasi>/<int:total_harga_penginapan>', receipt, name='receipt'),
]


