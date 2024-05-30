from rest_framework import serializers
from .models import Fullname, Address, Blood, Patient

class FullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fullname
        fields = ['id', 'first_name', 'last_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'no_house', 'street', 'ward', 'district', 'province']

class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = ['id', 'name']

class PatientSerializer(serializers.ModelSerializer):
    fullname = FullnameSerializer()
    address = AddressSerializer()
    blood = BloodSerializer()

    class Meta:
        model = Patient
        fields = ['id', 'date_of_birth', 'gender', 'mobile_number', 'email', 'allergies', 'medical_history', 'fullname', 'address', 'blood']
