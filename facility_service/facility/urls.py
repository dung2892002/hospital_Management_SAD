from .views import RoomAPIView, BedAPIView, SearchRoomAPIView, SearchBedAPIView, DeleteBedAPIView, UpdateRoomAPIView, UpdateBedAPIView
from django.urls import path

urlpatterns = [
    path('rooms/', RoomAPIView.as_view()),
    path('beds/', BedAPIView.as_view()),
    path('search-rooms', SearchRoomAPIView.as_view()),
    path('search-beds', SearchBedAPIView.as_view()),
    path('delete-bed/', DeleteBedAPIView.as_view()),
    path('update-room/', UpdateRoomAPIView.as_view()),
    path('update-bed/', UpdateBedAPIView.as_view())
]