from rest_framework import status
from django.db import models
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payment
from bill.models import Bill
from .serializers import PaymentSerializer

class PaymentCreateView(APIView):
    def get(self,request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            bill_id = request.data.get('bill')
            amount_paid = Payment.objects.filter(bill_id=bill_id).aggregate(total_amount_paid=models.Sum('payment_amount'))['total_amount_paid'] or 0
            total_price = Bill.objects.get(id=bill_id).total_price
            if amount_paid + serializer.validated_data['payment_amount'] > total_price:
                return Response({"error": f"Just pay {total_price - amount_paid} more"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SearchPaymentByBill(APIView):
    def get(self, request):
        bill_id = request.query_params.get('bill_id', None)
        if bill_id is not None:
            try:
                bill = Bill.objects.get(id=bill_id)
            except Bill.DoesNotExist:
                return Response({"error": "Bill not found"}, status=status.HTTP_404_NOT_FOUND)
            
            payments = Payment.objects.filter(bill = bill)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a bill_id"}, status=status.HTTP_400_BAD_REQUEST) 