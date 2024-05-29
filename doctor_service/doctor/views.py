from .models import Department, Position, Degree, Doctor, Fullname, Address
from .serializers import DepartmentSerializer, PositionSerializer, DegreeSerializer, FullnameSerializer, AddressSerializer, DoctorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class DepartmentAPIView(APIView):
    def get(self,request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
class DegreeAPIView(APIView):
    def get(self,request):
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DegreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        doctor_data = request.data
        fullname_data = doctor_data.pop('fullname')
        address_data = doctor_data.pop('address')

        fullname_serializer = FullnameSerializer(data=fullname_data)
        address_serializer = AddressSerializer(data=address_data)

        if fullname_serializer.is_valid() and address_serializer.is_valid():
            fullname = fullname_serializer.save()
            address = address_serializer.save()
            
            doctor = Doctor(
                fullname=fullname,
                address=address,
                mobile_number=doctor_data.get('mobile_number'),
                email=doctor_data.get('email'),
                department=Department.objects.get(id=doctor_data.get('department')),
                position=Position.objects.get(id=doctor_data.get('position')),
                degree=Degree.objects.get(id=doctor_data.get('degree'))
            )
            
            doctor.save()
            doctor_serializer = DoctorSerializer(doctor)
            return Response(doctor_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {
                "fullname": fullname_serializer.errors,
                "address": address_serializer.errors
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorDetailAPIView(APIView):
    def get(self, request):
        doctor_id = request.query_params.get('doctor_id', None)
        if doctor_id is not None:
            try:
                doctor = Doctor.objects.get(id=doctor_id)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a doctor_id"}, status=status.HTTP_400_BAD_REQUEST) 
        
class DoctorUpdateAPIView(APIView):        
    def put(self,request):
        doctor_id = request.data.get('id', None)
        if doctor_id is not None:
            try:
                doctor = Doctor.objects.get(id = doctor_id)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
            
            doctor_data = request.data
            fullname_data = doctor_data.pop('fullname')
            address_data = doctor_data.pop('address')
            
            fullname_serializer = FullnameSerializer(doctor.fullname, data=fullname_data)
            address_serializer = AddressSerializer(doctor.address, data=address_data)
            
            if fullname_serializer.is_valid() and address_serializer.is_valid():
                fullname = fullname_serializer.save()
                address = address_serializer.save()
                
                doctor.mobile_number = doctor_data.get('mobile_number', doctor.mobile_number)
                doctor.email = doctor_data.get('email', doctor.email)
                doctor.department_id = doctor_data.get('department', doctor.department_id)
                doctor.position_id = doctor_data.get('position', doctor.position_id)
                doctor.degree_id = doctor_data.get('degree', doctor.degree_id)
                doctor.fullname = fullname
                doctor.address = address
                
                doctor.save()
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data)
            else:
                errors = {
                    "fullname": fullname_serializer.errors,
                    "address": address_serializer.errors
                }
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Please provide a doctor_id"}, status=status.HTTP_400_BAD_REQUEST)
        
class DoctorDeleteAPIView(APIView):
    def delete(self,request):
        doctor_id = request.data.get('id', None)
        if doctor_id is not None:
            try:
                doctor = Doctor.objects.get(id = doctor_id)
            except Doctor.DoesNotExist:
                return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
            doctor.is_active = False
            doctor.save()
            return Response({"message": "Delete doctor success"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Please provide a doctor_id"}, status=status.HTTP_400_BAD_REQUEST)
            