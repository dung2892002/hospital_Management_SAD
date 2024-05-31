from .models import Position, Address, Fullname, Staff
from .serializers import PositionSerializer, FullnameSerializer, AddressSerializer, StaffSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class PositionAPIView(APIView):
    def get(self,request):
        positions = Position.objects.all()
        serializer = PositionSerializer(positions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StaffAPIView(APIView):
    def get(self, request):
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        staff_data = request.data
        fullname_data = staff_data.pop('fullname')
        address_data = staff_data.pop('address')

        fullname_serializer = FullnameSerializer(data=fullname_data)
        address_serializer = AddressSerializer(data=address_data)

        if fullname_serializer.is_valid() and address_serializer.is_valid():
            fullname = fullname_serializer.save()
            address = address_serializer.save()
            
            staff = Staff(
                fullname=fullname,
                address=address,
                mobile_number=staff_data.get('mobile_number'),
                email=staff_data.get('email'),
                position=Position.objects.get(id=staff_data.get('position')),
                
            )
            
            staff.save()
            staff_serializer = StaffSerializer(staff)
            return Response(staff_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {
                "fullname": fullname_serializer.errors,
                "address": address_serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)  

class StaffDetailAPIView(APIView):
    def get(self, request):
        staff_id = request.query_params.get('staff_id', None)
        if staff_id is not None:
            try:
                staff = Staff.objects.get(id=staff_id)
            except Staff.DoesNotExist:
                return Response({'error': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = StaffSerializer(staff)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a staff_id"}, status=status.HTTP_400_BAD_REQUEST) 

class StaffUpdateAPIView(APIView):        
    def put(self,request):
        staff_id = request.data.get('id', None)
        if staff_id is not None:
            try:
                staff = Staff.objects.get(id = staff_id)
            except Staff.DoesNotExist:
                return Response({'error': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)
            
            staff_data = request.data
            fullname_data = staff_data.pop('fullname')
            address_data = staff_data.pop('address')
            
            fullname_serializer = FullnameSerializer(staff.fullname, data=fullname_data)
            address_serializer = AddressSerializer(staff.address, data=address_data)
            
            if fullname_serializer.is_valid() and address_serializer.is_valid():
                fullname = fullname_serializer.save()
                address = address_serializer.save()
                
                staff.mobile_number = staff_data.get('mobile_number', staff.mobile_number)
                staff.email = staff_data.get('email', staff.email)
                staff.position_id = staff_data.get('position', staff.position_id)
                staff.fullname = fullname
                staff.address = address
                
                staff.save()
                serializer = StaffSerializer(staff)
                return Response(serializer.data)
            else:
                errors = {
                    "fullname": fullname_serializer.errors,
                    "address": address_serializer.errors
                }
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Please provide a staff_id"}, status=status.HTTP_400_BAD_REQUEST)

class StaffDeleteAPIView(APIView):
    def delete(self,request):
        staff_id = request.data.get('id', None)
        if staff_id is not None:
            try:
                staff = Staff.objects.get(id = staff_id)
            except Staff.DoesNotExist:
                return Response({'error': 'Staff not found'}, status=status.HTTP_404_NOT_FOUND)
            staff.is_active = False
            staff.save()
            return Response({"message": "Delete staff success"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Please provide a staff_id"}, status=status.HTTP_400_BAD_REQUEST)
            