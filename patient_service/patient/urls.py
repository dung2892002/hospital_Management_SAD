from .views import BloodAPIView, PatientAPIView, PatientDetailAPIView, PatientUpdateAPIView
from django.urls import path

urlpatterns = [
    path('bloods/', BloodAPIView.as_view()),
    path('patients/', PatientAPIView.as_view()),
    path('patients/detail/', PatientDetailAPIView.as_view()),
    path('patients/update/', PatientUpdateAPIView.as_view()),
]
