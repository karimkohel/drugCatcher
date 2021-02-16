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


def createAppointmet(request):
    if request.method == 'POST':
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
    else:
        form = AppointmentCreationForm()

    context = {
        'form':form,
        'title':"Create"
    }
    return render(request, 'home/createAppointment.html', context)


def load_companies(request):
    company_id = request.GET.get('company')
    companies = Company.objects.filter(country_id=company_id).order_by('name')
    return render(request, 'home/companyList.html', {'companies': companies})
