from django.contrib import admin
from .models import Personal, Appointment, Patient

# Register your models here.
admin.site.register(Personal)
admin.site.register(Appointment)
admin.site.register(Patient)
