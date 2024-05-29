from rest_framework import serializers
from .models import Department, Position, Degree, Fullname, Address, Doctor

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['id', 'name']

class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = ['id', 'first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'no_house', 'street', 'ward', 'district', 'province']

class DoctorSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    department = DepartmentSerializer()
    position = PositionSerializer()
    degree = DegreeSerializer()

    class Meta:
        model = Doctor
        fields = [
            'id',
            'mobile_number',
            'email',
            'is_active',
            'fullname',
            'address',
            'department',
            'position',
            'degree'
        ]
