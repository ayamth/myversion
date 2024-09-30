from django.urls import path
from .views import SignupView , HomeView


urlpatterns = [
    path('Singup/', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
]