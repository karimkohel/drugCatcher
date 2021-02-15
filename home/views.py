from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Appointment

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

# or better to do 

class CreateAppointment(CreateView):
    model = Appointment
    fields = '__all__'
    succes_url = reverse_lazy('index') # screen3
