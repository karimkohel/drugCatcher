from django.urls import path
from .views import index, CreateAppointment, load_companies

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('request', CreateAppointment.as_view(template_name='home/createAppointment.html'), name='createAppointment'),
    
    # AJAX for some ungodly reason
    path('ajax/load-companies', load_companies, name='ajaxLoadComp'),
]
