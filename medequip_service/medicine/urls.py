from .views import MedicineAPIView, SupplierAPIView, MedBatchAPIView, UpdateSoldQuantityAPIView, SearchBatchByMedicineAPIView
from django.urls import path

urlpatterns = [
    path('medicines/', MedicineAPIView.as_view()),
    path('suppliers/', SupplierAPIView.as_view()),
    path('med-batches/', MedBatchAPIView.as_view()),
    path('med-batches/medicine/', SearchBatchByMedicineAPIView.as_view()),
    path('med-batches/update/', UpdateSoldQuantityAPIView.as_view()),
]
