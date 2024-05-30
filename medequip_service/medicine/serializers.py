from rest_framework import serializers
from .models import Medicine, Supplier, MedBatch

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'price', 'description']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'email', 'phone', 'address']

class MedBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedBatch
        fields = ['id', 'medicine', 'supplier', 'quantity', 'sold', 'manufacture_date', 'expiration_date', 'received_date']
        
class MedBatchInfoSerializer(serializers.ModelSerializer):
    medicine = MedicineSerializer()
    supplier = SupplierSerializer()
    class Meta:
        model = MedBatch
        fields = ['id', 'medicine', 'supplier', 'quantity', 'sold', 'manufacture_date', 'expiration_date', 'received_date']
