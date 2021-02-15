from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Django's Moto is : Keep your Models fat and your Views small
# and i did just that

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Objective(models.Model):
    Type = models.CharField(max_length=60)

    def __str__(self):
        return self.Type

class Appointment(models.Model):

    firstName = models.CharField(max_length=30, help_text="First Name")
    lastName = models.CharField(max_length=30, help_text="Last Name")
    email = models.EmailField(help_text="Work Email Address")
    phoneNumber = PhoneNumberField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    objective = models.ForeignKey(Objective, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length='600')
    
    def __str__(self):
        return self.firstName + " " + self.lastName