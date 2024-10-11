from django.urls import path
from .views import customer_bill_list, mark_bill_paid, admin_bill_list

app_name = 'bills' 

urlpatterns = [
    path('customer/', customer_bill_list, name='customer_bill_list'),  
    path('mark-paid/<int:bill_id>/', mark_bill_paid, name='mark_bill_paid'),  
    path('admin/', admin_bill_list, name='admin_bill_list'),  
]
