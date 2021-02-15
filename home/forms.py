from django import forms
from .models import Appointment, Company

class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.fields['company'].queryset = Company.objects.none()
