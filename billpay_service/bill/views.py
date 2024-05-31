from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Bill, BillMedicine, BillMedicalService
from decimal import Decimal
from payment.models import Payment
from .serializers import BillSerializer,BillInfoSerializer
import requests

class BillAPIView(APIView):
    def get(self,request):
        bills = Bill.objects.all()
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        bill_data = request.data
        total_price = 0
        medicines_data = bill_data.pop('medicines')
        medical_services_data = bill_data.pop('medical_services')
        
        for medicine_data in medicines_data:
            response = self.validate(medicine_data)
            if (response.status_code == 200):
                data = response.json()
                value = data.get('total_price')
                total_price += value
            else:
                return Response({"error": f"Medicine with id {medicine_data['medicine_id']} has not enough {medicine_data['quantity']}"}, status=status.HTTP_400_BAD_REQUEST)
        
        for medical_service_data in medical_services_data:
            response = self.get_medical_service_info(medical_service_data)
            data = response.json()
            price = data.get('price')            
            total_price += int(medical_service_data['quantity']) * float(price)

        bill = Bill.objects.create(
            patient_id=bill_data.get('patient_id'),
            total_price=total_price
        )
        for medicine_data in medicines_data:
            BillMedicine.objects.create(
                medicine_id=medicine_data['medicine_id'],
                quantity=medicine_data['quantity'],
                bill=bill
            )
        for medical_service_data in medical_services_data:
            BillMedicalService.objects.create(
                medical_service_id=medical_service_data['medical_service_id'],
                quantity=medical_service_data['quantity'],
                bill=bill
            )
        return Response({"success": "Bill created successfully"}, status=status.HTTP_201_CREATED)

    def validate(self, medicine_data):
        medicine_id = medicine_data['medicine_id']
        quantity_purchased = medicine_data['quantity']
        response = requests.put(
            'http://localhost:8004/api/v1/med-batches/update/',
            data={'medicine_id': medicine_id, 'quantity': quantity_purchased}
        )
        return response
    
    def get_medical_service_info(self, medical_service_data):
        medical_service_id = medical_service_data['medical_service_id']
        response = requests.get("http://localhost:8004/api/v1/medical-services/detail/", params={'medical_service_id': medical_service_id})
        return response
    

class BillDetailAPIView(APIView):
    def get(self,request):
        bill_id = request.query_params.get('bill_id', None)
        if bill_id is not None:
            try:
                bill = Bill.objects.get(id=bill_id)
            except Bill.DoesNotExist:
                return Response({"error": "Bill not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = BillInfoSerializer(bill)
            medicines_data = serializer.data['medicines']
            medical_services_data = serializer.data['services']
            
            medicines = []
            medical_services = []
            
            for medicine_data in medicines_data:
                data = self.get_medicine_info(medicine_data['medicine_id'])
                medicines.append({
                    "name": data.get('name'),
                    "price": data.get('price'),
                    "quantity": medicine_data['quantity']
                })
                
            for medical_service_data in medical_services_data:
                data = self.get_medical_service_info(medical_service_data['medical_service_id'])
                medical_services.append({
                    "name": data.get('name'),
                    "price": data.get('price'),
                    "quantity": medicine_data['quantity']
                })
            patient= self.get_patient_info(serializer.data['patient_id'])
            payments = Payment.objects.filter(bill = bill)
            amount_paid = 0
            for payment in payments:
                amount_paid += payment.payment_amount
            response = {
                "patient": patient,
                "created_date": serializer.data['created_date'],
                "total_price": Decimal(serializer.data['total_price']),
                "amount_paid": amount_paid,
                "amount_owed": Decimal(serializer.data['total_price']) - amount_paid,
                "medicines" : medicines,
                "medical_services": medical_services,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response({"error": "Please provide a bill_id"}, status=status.HTTP_400_BAD_REQUEST) 

    def get_medicine_info(self, medicine_id):
        response = requests.get("http://localhost:8004/api/v1/medicines/detail/", params={'medicine_id': medicine_id})
        return response.json()
    
    def get_medical_service_info(self, medical_service_id):
        response = requests.get("http://localhost:8004/api/v1/medical-services/detail/", params={'medical_service_id': medical_service_id})
        return response.json()
    
    def get_patient_info(self, patient_id):
        response = requests.get("http://localhost:8002/api/v1/patients/detail/", params={'patient_id': patient_id})
        return response.json()
    
class SearchBillByPatientAPIView(APIView):
    def get(self, request):
        patient_id = request.query_params.get('patient_id', None)
        if patient_id is not None:
            bills = Bill.objects.filter(patient_id = patient_id)
            serializer = BillInfoSerializer(bills, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response({"error": "Please provide a bill_id"}, status=status.HTTP_400_BAD_REQUEST) 