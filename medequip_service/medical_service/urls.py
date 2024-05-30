from .views import MedicalServiceAPIView, MedicalServiceDetailAPIView, SearchByDepartmentAPIView, UpdateMedicalServiceAPIView
from django.urls import path

urlpatterns = [
    path('medical-services/', MedicalServiceAPIView.as_view()),
    path('medical-services/detail/', MedicalServiceDetailAPIView.as_view()),
    path('medical-services/department/', SearchByDepartmentAPIView.as_view()),
    path('medical-services/update/', UpdateMedicalServiceAPIView.as_view()),
]
