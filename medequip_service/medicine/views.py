from rest_framework import status
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Medicine, Supplier, MedBatch
from .serializers import MedicineSerializer, SupplierSerializer, MedBatchSerializer, MedBatchInfoSerializer

class SupplierAPIView(APIView):
    def get(self, request):
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = SupplierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineAPIView(APIView):
    def get(self, request):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedBatchAPIView(APIView):
    def get(self, request):
        med_batches = MedBatch.objects.all()
        serializer = MedBatchInfoSerializer(med_batches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = MedBatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSoldQuantityAPIView(APIView):
    def put(self, request):
        medicine_id = request.data.get('medicine_id')
        quantity_purchased = request.data.get('quantity')

        if not medicine_id or not quantity_purchased:
            return Response({"error": "Please provide medicine_id and quantity"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            medicine = Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return Response({"error": "Medicine not found"}, status=status.HTTP_404_NOT_FOUND)

        med_batches = MedBatch.objects.filter(medicine=medicine, quantity__gt=models.F('sold')).order_by('quantity')

        total_sold = sum(batch.sold for batch in med_batches)

        total_quantity = sum(batch.quantity for batch in med_batches)

        if int(quantity_purchased) > (total_quantity - total_sold):
            return Response({"error": "Quantity purchased exceeds available stock"}, status=status.HTTP_400_BAD_REQUEST)
        
        for batch in med_batches:
            if quantity_purchased <= 0:
                break
            available_quantity = batch.quantity - batch.sold
            if available_quantity >= quantity_purchased:
                batch.sold += quantity_purchased
                batch.save()
                break
            else:
                batch.sold = batch.quantity
                batch.save()
                quantity_purchased -= available_quantity
        
        return Response({"success": "Sold quantity updated successfully"}, status=status.HTTP_200_OK)


class SearchBatchByMedicineAPIView(APIView):
    def get(self, request):
        medicine_id = request.query_params.get('medicine_id', None)
        
        if not medicine_id:
            return Response({"error": "Please provide medicine_id"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            medicine = Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return Response({"error": "Medicine not found"}, status=status.HTTP_404_NOT_FOUND)
        
        med_batches = MedBatch.objects.filter(medicine=medicine, quantity__gt=models.F('sold')).order_by('quantity')
        serializer = MedBatchInfoSerializer(med_batches, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
