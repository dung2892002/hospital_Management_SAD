from .serializers import MedicalRecordSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import MedicalRecord

class MedicalRecordAPIView(APIView):
    def get(self,request):
        medicalRecord = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(medicalRecord, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchMedicalRecordAPIView(APIView):
    def get(self, request):
        patientID_param = request.query_params.get('patient_id', None)
        doctorID_param = request.query_params.get('doctor_id', None)

        medicalRecords = MedicalRecord.objects.all()

        if patientID_param is not None:
            medicalRecords = medicalRecords.filter(patient_id=patientID_param)
        
        if doctorID_param is not None:
            medicalRecords = medicalRecords.filter(doctor_id=doctorID_param)

        serializer = MedicalRecordSerializer(medicalRecords, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateMedicalRecordAPIView(APIView):
    def put(self, request):
        try:
            data = request.data
            medicalRecordID = data.get('medicalrecord_id', None)
            
            if medicalRecordID is None:
                return Response({"error": "MedicalRecordID is required"}, status=status.HTTP_400_BAD_REQUEST)

            medicalRecord = MedicalRecord.objects.get(id=medicalRecordID)
            serializer = MedicalRecordSerializer(medicalRecord, data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except MedicalRecord.DoesNotExist:
            return Response({"error": "MedicalRecord not found"}, status=status.HTTP_404_NOT_FOUND)