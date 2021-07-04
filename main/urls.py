from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('filterPencarian', views.filterPencarian, name='filterPencarian'),
    path('data/basedOnReservasi/', views.data_basedOnReservasi, name='data_basedOnReservasi'),
]
