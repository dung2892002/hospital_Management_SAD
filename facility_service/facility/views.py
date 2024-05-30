from django.shortcuts import render
from .serializers import RoomSerializer, BedSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Room, Bed
import json

class RoomAPIView(APIView):
    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BedAPIView(APIView):    
    def post(self, request):
        serializer = BedSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SearchRoomAPIView(APIView):    
    def get(self, request):
            status_param = request.query_params.get('status', None)
            room_type_param = request.query_params.get('room_type', None)
            capacity_param = request.query_params.get('capacity', None)

            rooms = Room.objects.all()

            if status_param is not None:
                rooms = rooms.filter(status=status_param == 'true')
            
            if room_type_param is not None:
                rooms = rooms.filter(room_type=room_type_param)
            
            if capacity_param is not None:
                rooms = rooms.filter(capacity=capacity_param)

            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
class SearchBedAPIView(APIView):
    def get(self, request):
        status_param = request.query_params.get('status', None)
        room_id_param = request.query_params.get('room_id', None)

        beds = Bed.objects.all()

        if status_param is not None:
            beds = beds.filter(status=status_param == 'true')
        
        if room_id_param is not None:
            beds = beds.filter(room_id=room_id_param)

        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class DeleteBedAPIView(APIView):

    def delete(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            bed_id = data.get('bed_id', None)

            if bed_id is None:
                return Response({"error": "bed_id is required"}, status=status.HTTP_400_BAD_REQUEST)

            bed = Bed.objects.get(id=bed_id)
            bed.delete()
            return Response({"message": "delete bed success!"},status=status.HTTP_200_OK)
        except Bed.DoesNotExist:
            return Response({"error": "Bed not found"}, status=status.HTTP_404_NOT_FOUND)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON"}, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateRoomAPIView(APIView):

    def put(self, request):
        try:
            data = request.data
            room_id = data.get('room_id', None)
            
            if room_id is None:
                return Response({"error": "room_id is required"}, status=status.HTTP_400_BAD_REQUEST)

            room = Room.objects.get(id=room_id)
            serializer = RoomSerializer(room, data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdateBedAPIView(APIView):
    def put(self, request):
        try:
            data = request.data
            bed_id = data.get('id', None)  
            room_id = data.get('room_id', None)
            if bed_id is None:
                return Response({"error": "id bed is required"}, status=status.HTTP_400_BAD_REQUEST)

            bed = Bed.objects.get(id=bed_id)
            room = Room.objects.get(id=room_id)
            room_capacity = room.capacity
        
            
            # Update bed
            serializer = BedSerializer(bed, data=data)
            if serializer.is_valid():
                serializer.save()

                # Count beds with status=true in the same room
                active_beds_count = Bed.objects.filter(room_id=room.id, status=True).count()

                # Check if the room's status needs to be updated
                if active_beds_count == room_capacity:
                    room.status = True
                    room.save()
                elif (active_beds_count != room_capacity):
                    room.status = False
                    room.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Bed.DoesNotExist:
            return Response({"error": "Bed not found"}, status=status.HTTP_404_NOT_FOUND)

        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)
