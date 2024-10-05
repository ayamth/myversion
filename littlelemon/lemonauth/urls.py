from django.urls import path
from .views import SignupView , HomeView , LogunView ,CustomLogoutViews, OrdersView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('Singup/', SignupView.as_view(), name='signup'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LogunView.as_view(), name='login'),
    path('logout/', CustomLogoutViews.as_view(), name='logout'),
     path('orders/', OrdersView.as_view(), name='orders'),
]
