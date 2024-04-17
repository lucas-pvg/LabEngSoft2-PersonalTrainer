from rest_framework import serializers
from .models import *


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
        

class EvaluationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = "__all__"
        
        
class EvolutionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evolution
        fields = "__all__"
        
        
class DietSerializers(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = "__all__"
        

class TrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"
