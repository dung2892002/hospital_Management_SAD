from rest_framework import serializers
from .models import MedicalService

class MedicalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalService
        fields = ['id', 'name', 'price', 'description', 'department_id']