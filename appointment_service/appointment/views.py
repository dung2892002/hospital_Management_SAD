from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer
from django.shortcuts import get_object_or_404
import requests

def get_patient_info(patient_id):
        try:
            response = requests.get(f"http://localhost:8002/api/v1/patients/detail/?patient_id={patient_id}")
            if response.status_code == 200:
                return response.json()
            return {"error": "Could not fetch patient info"}
        except requests.RequestException as e:
            return {"error": str(e)}

def get_doctor_info(doctor_id):
    try:
        response = requests.get(f"http://localhost:8001/api/v1/doctors/detail/?doctor_id={doctor_id}")
        if response.status_code == 200:
            return response.json()
        return {"error": "Could not fetch doctor info"}
    except requests.RequestException as e:
        return {"error": str(e)}

class AppointmentAPIView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            patient_id = request.data.get('patient_id')
            doctor_id = request.data.get('doctor_id')
            
            patient_info = get_patient_info(patient_id)
            doctor_info = get_doctor_info(doctor_id)
            if 'error' in patient_info:
                return Response({"error": "Patient does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            if 'error' in doctor_info:
                return Response({"error": "Doctor does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            if doctor_info.get('is_active', False) is False:
                return Response({"error": "Doctor is not active."}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetailAPIView(APIView):
    def get(self, request):
        appointment_id = request.query_params.get('appointment_id', None)
        if appointment_id is not None:
            appointment = get_object_or_404(Appointment, id=appointment_id)
            serializer = AppointmentSerializer(appointment)
            
            patient_id = appointment.patient_id
            doctor_id = appointment.doctor_id
            
            patient_info = get_patient_info(patient_id)
            doctor_info = get_doctor_info(doctor_id)
            
            data = serializer.data
            data['patient_info'] = patient_info
            data['doctor_info'] = doctor_info
            
            return Response(data, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a appointment_id"}, status=status.HTTP_400_BAD_REQUEST) 

class AppointmentStatusUpdateAPIView(APIView):
    def put(self, request):
        appointment_id = request.data.get('appointment_id', None)
        new_status = request.data.get('status', None)

        if appointment_id is not None and new_status is not None:
            try:
                appointment = Appointment.objects.get(id=appointment_id)
            except Appointment.DoesNotExist:
                return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)

            appointment.status = new_status
            appointment.save()

            serializer = AppointmentSerializer(appointment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error": "Please provide both appointment_id and status"}, status=status.HTTP_400_BAD_REQUEST)

class AppointmentSearchByDoctorAPIView(APIView):
    def get(self, request):
        doctor_id = request.query_params.get('doctor_id', None)
        if doctor_id is not None:
            appointments = Appointment.objects.filter(doctor_id=doctor_id)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a doctor_id"}, status=status.HTTP_400_BAD_REQUEST)

class AppointmentSearchByPatientAPIView(APIView):
    def get(self, request):
        patient_id = request.query_params.get('patient_id', None)
        if patient_id is not None:
            appointments = Appointment.objects.filter(patient_id=patient_id)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a patient_id"}, status=status.HTTP_400_BAD_REQUEST)