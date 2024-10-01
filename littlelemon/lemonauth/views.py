from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import SignupForm ,LoginForm
from django.views.generic import FormView ,TemplateView
from django.urls import reverse_lazy



class SignupView (FormView):
    form_class= SignupForm
    template_name ='lemonauth/signup.html'
    success_url =reverse_lazy('login')

    def form_valid(self,form):
        print("form valid and will be save")
        form.save()
        return super().form_valid(form)


    def form_invalid(self, form):
        print("form invalid")
        print(form.errors) 
        return super().form_invalid(form)
    
class HomeView(TemplateView):
    template_name = 'lemonauth/home.html'

class LogunView (LoginView):
    form_class= LoginForm
    template_name = 'lemonauth/index.html'
    success_url = reverse_lazy('home') 
    

