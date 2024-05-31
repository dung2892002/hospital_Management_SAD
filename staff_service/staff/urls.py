from .views import  PositionAPIView, StaffAPIView, StaffDetailAPIView, StaffUpdateAPIView, StaffDeleteAPIView
from django.urls import path

urlpatterns = [
    path('staff/positions/', PositionAPIView.as_view()),
    path('staffs/', StaffAPIView.as_view()),
    path('staffs/detail/', StaffDetailAPIView.as_view()),
    path('staffs/update/', StaffUpdateAPIView.as_view()),
    path('staffs/delete/', StaffDeleteAPIView.as_view()),
]