from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Appointment

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def appointmentReq(request):
    return render(request, 'home/appReq.html')

# or better to do 

# class CreateAppointment(CreateView):
#     model = Appointment

# and create an ajax view to change company 