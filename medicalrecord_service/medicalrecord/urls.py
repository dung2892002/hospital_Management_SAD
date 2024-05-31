from .views import MedicalRecordAPIView, SearchMedicalRecordAPIView, UpdateMedicalRecordAPIView
from django.urls import path

urlpatterns = [
    path('medicalrecords/', MedicalRecordAPIView.as_view()),
    path('medicalrecords/', SearchMedicalRecordAPIView.as_view()),
    path('update-medicalrecord/', UpdateMedicalRecordAPIView.as_view()),
]