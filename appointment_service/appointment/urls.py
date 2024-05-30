from .views import AppointmentAPIView, AppointmentDetailAPIView, AppointmentStatusUpdateAPIView, AppointmentSearchByPatientAPIView, AppointmentSearchByDoctorAPIView
from django.urls import path

urlpatterns = [
    path('appointments/', AppointmentAPIView.as_view()),
    path('appointments/detail/', AppointmentDetailAPIView.as_view()),
    path('appointments/doctor/', AppointmentSearchByDoctorAPIView.as_view()),
    path('appointments/patient/', AppointmentSearchByPatientAPIView.as_view()),
    path('appointments/update/', AppointmentStatusUpdateAPIView.as_view()),
]
