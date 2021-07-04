from django.urls import path

from . import views

app_name = 'aboutuser'

urlpatterns = [
    path('profil/', views.profil, name='profil'),
    path('review/<str:idtransaksi>/', views.review, name='review'),
    path('data/myreview/', views.dataMyReview, name='dataMyReview'),

]
