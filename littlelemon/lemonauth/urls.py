from django.urls import path
from .views import SignupView , HomeView , LogunView


urlpatterns = [
    path('Singup/', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LogunView.as_view(), name='login'),
]