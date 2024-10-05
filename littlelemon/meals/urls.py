from django.urls import path
from .views import MealsListView, MealsDetailView, MealsCreateView, MealsUpdateView, MealsDeleteView

urlpatterns = [
    path('', MealsListView.as_view(), name='meals_list'),  # لعرض كل الوجبات
    path('<int:pk>/', MealsDetailView.as_view(), name='meals_detail'),  # عرض تفاصيل وجبة
    path('create/', MealsCreateView.as_view(), name='meals_create'),  # إنشاء وجبة جديدة
    path('update/<int:pk>/', MealsUpdateView.as_view(), name='meals_update'),  # تعديل وجبة
    path('delete/<int:pk>/', MealsDeleteView.as_view(), name='meals_delete'),  # حذف وجبة
]