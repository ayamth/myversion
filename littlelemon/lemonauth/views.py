from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import SignupForm
from django.views.generic import FormView ,TemplateView
from django.urls import reverse_lazy



class SignupView (FormView):
    form_class= SignupForm
    template_name ='lemonauth/index.html'
    success_url = reverse_lazy('home')

    def form_valid(self ,form):
        form.save()
        return super().form_valid(form)
    
class HomeView(TemplateView):
    template_name = 'lemonauth/home.html'
    

