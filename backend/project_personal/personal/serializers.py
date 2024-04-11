from rest_framework import serializers
from .models import Patient, Personal, Appointment


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields ="__all__"
        

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
