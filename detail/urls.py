from django.urls import path
from detail.views import *
from detail.views2 import *

app_name = 'detail'
urlpatterns = [
    path('', hasil_pencarian, name='hasil_pencarian'),
    path('detailpencarian/<str:id>/<str:checkin>/<str:checkout>/<str:jml>/', detailpencarian, name='detailpencarian'),
    path('getkodefromcheckin/<str:id>/<str:checkin>/<str:checkout>/<str:jml>/', getkodefromcheckin, name='getkodefromcheckin'),

]

