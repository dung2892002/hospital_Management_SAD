from .views import DepartmentAPIView, PositionAPIView, DegreeAPIView, DoctorAPIView, DoctorDetailAPIView, DoctorUpdateAPIView, DoctorDeleteAPIView
from django.urls import path

urlpatterns = [
    path('departments/', DepartmentAPIView.as_view()),
    path('positions/', PositionAPIView.as_view()),
    path('degrees/', DegreeAPIView.as_view()),
    path('doctors/', DoctorAPIView.as_view()),
    path('doctors/detail/', DoctorDetailAPIView.as_view()),
    path('doctors/update/', DoctorUpdateAPIView.as_view()),
    path('doctors/delete/', DoctorDeleteAPIView.as_view()),
]
