from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Personal, Patient, Appointment
from .serializers import PersonalSerializer, PatientSerializer, AppointmentSerializer


class PersonalView(ViewSet):
    def create(self, request):
        serializer = PersonalSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Personal.objects.create(**serializer.validated_data)
        serializer = PersonalSerializer(queryset)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    def list_all(self, request):
        queryset = Personal.objects.all()
        serializer = PersonalSerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Personal.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PersonalSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PatientView(ViewSet):
    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        queryset = Patient.objects.create(**serializer.validated_data)
        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def list_all(self, request):
        queryset = Patient.objects.all()
        serializer = PatientSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list_from_personal(self, request):
        patient_list = request.data['patient_list']
        queryset = Patient.objects.filter(pk__in=patient_list)
        serializer = PatientSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk):
        queryset = Patient.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AppointmentView(ViewSet):
    def create(self, request):
        serializer = AppointmentSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Appointment.objects.create(**serializer.validated_data)
        serializer = AppointmentSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def list_all(self, request):
        queryset = Appointment.objects.all()
        serializer = AppointmentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def list_from_personal(self, request, prof):
        queryset = Appointment.objects.filter(professional=prof)
        serializer = AppointmentSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def retrieve(self, request, pk):
        queryset = Appointment.objects.filter(pk=pk).first()

        if not queryset:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AppointmentSerializer(queryset)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ExerciseView(ViewSet):
    pass


class PaymentView(ViewSet):
    pass
