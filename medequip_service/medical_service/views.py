from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MedicalService
from .serializers import MedicalServiceSerializer

class MedicalServiceAPIView(APIView):
    def get(self, request):
        medical_services = MedicalService.objects.all()
        serializer = MedicalServiceSerializer(medical_services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = MedicalServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicalServiceDetailAPIView(APIView):
    def get(self, request):
        medical_service_id = request.query_params.get('medical_service_id', None)
        if medical_service_id is not None:
            medical_service = get_object_or_404(MedicalService, id=medical_service_id)
            serializer = MedicalServiceSerializer(medical_service)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a medical_service_id"}, status=status.HTTP_400_BAD_REQUEST) 

class UpdateMedicalServiceAPIView(APIView):
    def put(self, request):
        medical_service_id = request.data.get('id', None)
        
        if medical_service_id is None:
            return Response({"error": "Please provide medical_service_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            equipment = MedicalService.objects.get(id=medical_service_id)
        except MedicalService.DoesNotExist:
            return Response({"error": "MedicalService not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MedicalServiceSerializer(equipment, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class SearchByDepartmentAPIView(APIView):
    def get(self, request):
        department_id = request.query_params.get('department_id', None)
        if department_id is None:
            return Response({"error": "Please provide department_id"}, status=status.HTTP_400_BAD_REQUEST)
        medical_services = MedicalService.objects.filter(department_id = department_id)
        serializer = MedicalServiceSerializer(medical_services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

