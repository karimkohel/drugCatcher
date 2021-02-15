from django.contrib import admin
from home.models import Appointment, Company, Country, Objective

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Objective)
