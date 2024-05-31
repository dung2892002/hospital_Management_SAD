from rest_framework import serializers
from .models import Bill, BillMedicine, BillMedicalService


class BillMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillMedicine
        fields = ['id', 'medicine_id', 'quantity']

class BillMedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillMedicalService
        fields = ['id', 'medical_service_id', 'quantity']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'patient_id', 'created_date', 'total_price']
        
class BillInfoSerializer(serializers.ModelSerializer):
    medicines = BillMedicineSerializer(many=True, read_only=True)
    services = BillMedicalServiceSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ['id', 'patient_id', 'created_date', 'total_price', 'medicines', 'services']
