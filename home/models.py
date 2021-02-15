from django.db import models

# Create your models here.
class Appointment(models.Model):
    firstName = models.CharField(max_length=30, help_text="First Name")
    lastName = models.CharField(max_length=30, help_text="Last Name")
    email = models.EmailField(help_text="Work Email Address")

