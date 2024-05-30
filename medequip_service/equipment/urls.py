from .views import EquipmentAPIView, EquipmentDetailAPIView, SearchByDepartmentAPIView, UpdateEquipmentAPIView
from django.urls import path

urlpatterns = [
    path('equipments/', EquipmentAPIView.as_view()),
    path('equipments/detail/', EquipmentDetailAPIView.as_view()),
    path('equipments/department/', SearchByDepartmentAPIView.as_view()),
    path('equipments/update/', UpdateEquipmentAPIView.as_view()),
]
