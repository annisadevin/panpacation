from django.urls import path

from . import views

app_name = 'aboutuser'

urlpatterns = [
    path('profil/', views.profil, name='profil'),
]
