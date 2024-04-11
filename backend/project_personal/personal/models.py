from django.db import models

APP_OPTIONS = (
    ('0', 'CANCELED'),
    ('1', 'PENDING'),
    ('2', 'CONFIRMED'),
)

# Create your models here.    
class Patient(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    document = models.CharField(max_length=15, unique=True, blank=True, null=True)
    height = models.DecimalField(decimal_places=2, max_digits=3, null=True, blank=True)
    weight = models.PositiveIntegerField(null=True, blank=True)
    bmi = models.PositiveIntegerField(null=True, blank=True)
    history = models.TextField(max_length=500, null=True, blank=True)
    
    
class Personal(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    document = models.CharField(max_length=15, unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False)
    is_online = models.BooleanField(default=1, null=False, blank=False)
    summary = models.TextField(max_length=500, null=True, blank=True)
    patients = models.ManyToManyField(Patient, blank=True, null=True)


class Appointment(models.Model):
    professional = models.ForeignKey(Personal, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments", null=True, blank=True)
    datetime = models.DateTimeField(null=False, blank=False)
    is_online = models.BooleanField(null=False, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=APP_OPTIONS, null=True, blank=True)


class Exercise(models.Model):
    pass


class Payment(models.Model):
    pass
