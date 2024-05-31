from .models import Position, Address, Fullname, Staff
from rest_framework import serializers

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name']
        
class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = ['id', 'first_name', 'last_name']
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'no_house', 'street', 'ward', 'district', 'province']

class StaffSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    position = PositionSerializer()

    class Meta:
        model = Staff
        fields = [
            'id',
            'mobile_number',
            'email',
            'is_active',
            'fullname',
            'address',
            'position',
        ]