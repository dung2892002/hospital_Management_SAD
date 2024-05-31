from django.urls import path
from .views import PaymentCreateView, SearchPaymentByBill

urlpatterns = [
    path('payments/', PaymentCreateView.as_view()),
    path('payments/bill/', SearchPaymentByBill.as_view()),
]
