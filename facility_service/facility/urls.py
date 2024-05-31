from .views import RoomAPIView, BedAPIView, SearchRoomAPIView, SearchBedAPIView, DeleteBedAPIView, UpdateRoomAPIView, UpdateBedAPIView
from django.urls import path

urlpatterns = [
    path('rooms/', RoomAPIView.as_view()),
    path('beds/', BedAPIView.as_view()),
    path('rooms/search/', SearchRoomAPIView.as_view()),
    path('beds/search/', SearchBedAPIView.as_view()),
    path('beds/delete/', DeleteBedAPIView.as_view()),
    path('rooms/update/', UpdateRoomAPIView.as_view()),
    path('beds/update/', UpdateBedAPIView.as_view())
]