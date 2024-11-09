from django.urls import path
from . import views
from .views import ReservationListApiView, ReservationDetailApiView

urlpatterns = [
    path('', views.template, name='template'),
    path('list/', views.list_reservations, name='reservation_list'),  # List all reservations
    path('new/', views.create_reservation, name='create_reservation'),  # Create a new reservation
    path('<int:pk>/edit/', views.update_reservation, name='update_reservation'),  # Edit a reservation
    path('<int:pk>/delete/', views.delete_reservation, name='delete_reservation'),  # Delete a reservation
    path('api/reservations/', ReservationListApiView.as_view(), name='reservation_list_api'),
    path('api/reservations/<int:pk>/', ReservationDetailApiView.as_view(), name='reservation_detail_api'),
]

