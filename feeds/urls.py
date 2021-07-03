from django.urls import path

from . import views

app_name = 'feeds'

urlpatterns = [
    path('feeds/', views.feeds, name='feeds'),
]
