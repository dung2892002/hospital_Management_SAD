from .views import MedicalRecordAPIView, SearchMedicalRecordAPIView, UpdateMedicalRecordAPIView
from django.urls import path

urlpatterns = [
    path('medical-records/', MedicalRecordAPIView.as_view()),
    path('medical-records/search/', SearchMedicalRecordAPIView.as_view()),
    path('medical-records/update/', UpdateMedicalRecordAPIView.as_view()),
]