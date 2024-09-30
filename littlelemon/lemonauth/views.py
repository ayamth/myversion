from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy



class CustomLoginView(LoginView):
    template_name = 'lemonauth/index.html'
    

