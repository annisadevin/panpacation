from django.urls import path
from detail.views import *
from detail.views2 import *

app_name = 'detail'
urlpatterns = [
    path('', hasil_pencarian, name='hasil_pencarian'),
    path('detail_pencarian/', detail_pencarian, name='detail_pencarian'),
]

