from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from .models import Appointment, Company
from .forms import AppointmentCreationForm

# Create your views here.

def index(request):
    return render(request, 'home/index.html')


class CreateAppointment(CreateView):
    model = Appointment
    form_class = AppointmentCreationForm
    success_message = "Appointment was set successfully"
    succes_url = reverse_lazy('home:confirm')

    def get_success_url(self):
        return reverse('home:confirm')
    



def load_companies(request):
    country_id = request.GET.get('country')
    companies = Company.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'home/companyList.html', {'companies': companies})

def confirm(request):
    context = {'title': 'Confirm'}
    return render(request, "home/confirm.html", context)