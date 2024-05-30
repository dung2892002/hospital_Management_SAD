from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Equipment
from .serializers import EquipmentSerializer

class EquipmentAPIView(APIView):
    def get(self, request):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipmentDetailAPIView(APIView):
    def get(self, request):
        equipment_id = request.query_params.get('equipment_id', None)
        if equipment_id is not None:
            equipment = get_object_or_404(Equipment, id=equipment_id)
            serializer = EquipmentSerializer(equipment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a equipment_id"}, status=status.HTTP_400_BAD_REQUEST) 

class UpdateEquipmentAPIView(APIView):
    def put(self, request):
        equipment_id = request.data.get('id', None)
        
        if equipment_id is None:
            return Response({"error": "Please provide equipment_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            equipment = Equipment.objects.get(id=equipment_id)
        except Equipment.DoesNotExist:
            return Response({"error": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EquipmentSerializer(equipment, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class SearchByDepartmentAPIView(APIView):
    def get(self, request):
        department_id = request.query_params.get('department_id', None)
        if department_id is None:
            return Response({"error": "Please provide department_id"}, status=status.HTTP_400_BAD_REQUEST)
        equipments = Equipment.objects.filter(department_id = department_id)
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

