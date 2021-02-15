from django.urls import path
from .views import index, appointmentReq

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('request', appointmentReq, name='appReq'),
]
