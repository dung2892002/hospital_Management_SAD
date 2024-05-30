from rest_framework import serializers
from .models import Room, Bed

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        
class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        fields = "__all__"