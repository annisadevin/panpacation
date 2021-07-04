from django.urls import path
from pembayaran.views import *

app_name = 'pembayaran'
urlpatterns = [
    path('buatpesanan/<str:id_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<int:total_penginap>/', buatpesanan, name='buatpesanan'),
    path('metodebayar/<str:nama_pemesan>/<str:id_penginapan>/<str:nama_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<str:durasi>/<str:total_pesanan>/<str:harga_test_covid>/<str:total_semua>/<str:no_telp>/<str:total_penginap>/', metodebayar, name='metodebayar'),
    path('receipt/<str:nama_pemesan>/<str:id_penginapan>/<str:nama_penginapan>/<str:tgl_checkin>/<str:tgl_checkout>/<str:durasi>/<str:total_pesanan>/<str:harga_test_covid>/<str:total_semua>/<str:no_telp>/<str:total_penginap>/', receipt, name='receipt'),
]
