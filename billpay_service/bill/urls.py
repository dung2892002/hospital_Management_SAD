from .views import BillAPIView, BillDetailAPIView, SearchBillByPatientAPIView
from django.urls import path

urlpatterns = [
    path('bills/', BillAPIView.as_view()),
    path('bills/detail/', BillDetailAPIView.as_view()),
    path('bills/patient/', SearchBillByPatientAPIView.as_view())
]
