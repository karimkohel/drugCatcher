from django.urls import path
from .views import index, CreateAppointment

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('request', CreateAppointment.as_view(template_name='home/createAppointment.html'), name='createAppointment'),
]
