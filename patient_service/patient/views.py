from .models import Blood, Patient
from .serializers import FullnameSerializer, AddressSerializer, BloodSerializer, PatientSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

class BloodAPIView(APIView):
    def get(self,request):
        bloods = Blood.objects.all()
        serializer = BloodSerializer(bloods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BloodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientAPIView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        patient_data = request.data
        fullname_data = patient_data.pop('fullname')
        address_data = patient_data.pop('address')
        
        fullname_serializer = FullnameSerializer(data=fullname_data)
        address_serializer = AddressSerializer(data=address_data)
        
        if fullname_serializer.is_valid() and address_serializer.is_valid():
            fullname = fullname_serializer.save()
            address = address_serializer.save()
            
            blood = get_object_or_404(Blood, id=patient_data.get('blood'))
            patient = Patient(
                fullname=fullname,
                address=address,
                blood=blood,
                date_of_birth=patient_data.get('date_of_birth'),
                gender=patient_data.get('gender'),
                mobile_number=patient_data.get('mobile_number'),
                email=patient_data.get('email'),
                allergies=patient_data.get('allergies', ''),
                medical_history=patient_data.get('medical_history', '')
            )
            
            patient.save()
            patient_serializer = PatientSerializer(patient)
            return Response(patient_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {
                "fullname": fullname_serializer.errors,
                "address": address_serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class PatientDetailAPIView(APIView):
    def get(self, request):
        patient_id = request.query_params.get('patient_id', None)
        if patient_id is not None:
            patient = get_object_or_404(Patient, id=patient_id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a patient_id"}, status=status.HTTP_400_BAD_REQUEST) 
        
class PatientUpdateAPIView(APIView):
    def put(self, request):
        patient_id = request.data.get('id', None)
        if patient_id is not None:
            try:
                patient = Patient.objects.get(id=patient_id)
            except Patient.DoesNotExist:
                return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
            
            patient_data = request.data
            fullname_data = patient_data.pop('fullname')
            address_data = patient_data.pop('address')
            
            fullname_serializer = FullnameSerializer(patient.fullname, data=fullname_data)
            address_serializer = AddressSerializer(patient.address, data=address_data)
            
            if fullname_serializer.is_valid() and address_serializer.is_valid():
                fullname_serializer.save()
                address_serializer.save()
                
                patient.date_of_birth = patient_data.get('date_of_birth', patient.date_of_birth)
                patient.gender = patient_data.get('gender', patient.gender)
                patient.mobile_number = patient_data.get('mobile_number', patient.mobile_number)
                patient.email = patient_data.get('email', patient.email)
                patient.allergies = patient_data.get('allergies', patient.allergies)
                patient.medical_history = patient_data.get('medical_history', patient.medical_history)
                
                blood_id = patient_data.get('blood', patient.blood_id)
                if blood_id:
                    patient.blood = Blood.objects.get(id=blood_id)
                
                patient.save()
                serializer = PatientSerializer(patient)
                return Response(serializer.data)
            else:
                errors = {
                    "fullname": fullname_serializer.errors,
                    "address": address_serializer.errors
                }
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Please provide a patient_id"}, status=status.HTTP_400_BAD_REQUEST)
