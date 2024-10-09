from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Meals
from .forms import MealsForm
from django.contrib import messages


class MealsListView(ListView):
    model = Meals
    template_name = 'meals_list.html' 
    

    def get_queryset(self):
        return Meals.objects.filter(available=True)
    


class MealsDetailView(DetailView):
    model = Meals
    template_name = 'meals_detail.html'  
    context_object_name = 'meal'


class MealsCreateView(CreateView):
    model = Meals
    form_class = MealsForm
    template_name = 'meals_form.html' 
    success_url = reverse_lazy('meals_list')

    def form_valid(self, form):
        messages.success(self.request, "Meal has been successfully added!")
        return super().form_valid(form)


class MealsUpdateView(UpdateView):
    model = Meals
    form_class = MealsForm
    template_name = 'meals_form.html'  
    success_url = reverse_lazy('meals_list')


    def form_valid(self, form):
        messages.success(self.request, "Meal has been successfully dupdated!")
        return super().form_valid(form)


class MealsDeleteView(DeleteView):
    model = Meals
    template_name = 'meals_confirm_delete.html' 
    success_url = reverse_lazy('meals_list')

    def form_valid(self, form):
        messages.success(self.request, "Meal has been successfully deleted!")
        return super().form_valid(form)