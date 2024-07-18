
from django.urls import path

from hotels import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/new/', views.room_create, name='room_create'),
    path('room/<int:pk>/edit/', views.room_edit, name='room_edit'),
    path('room/<int:pk>/delete/', views.room_delete, name='room_delete'),
    path('booking/new/', views.booking_create, name='booking_create'),
    path('booking/', views.booking_list, name='booking_list'),
]
