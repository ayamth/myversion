from django.contrib import admin
from .models import Meals

@admin.register(Meals)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')  # Customize as needed


