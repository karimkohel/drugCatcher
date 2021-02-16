from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Appointment, Company
from .forms import AppointmentCreationForm

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

# or better to do 

class CreateAppointment(CreateView):
    model = Appointment
    form_class = AppointmentCreationForm
    succes_url = reverse_lazy('index') # screen3


def load_companies(request):
    country_id = request.GET.get('country')
    companies = Company.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'home/companyList.html', {'companies': companies})