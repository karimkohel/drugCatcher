from django import forms
from .models import Appointment, Company, Country, Objective

class AppointmentCreationForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['firstName', 'lastName', 'email', 'phoneNumber', 'country', 'company', 'objective', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.none()
        
        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['company'].queryset = Company.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['company'].queryset = self.instance.country.company_set.order_by('name')