from django.conf import settings
from django.db import models
from bills.models import Bill
from meals.models import Meals

class Orders(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)  # Allow null temporarily
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.meal.name}(s) by {self.customer.username}"

    def get_total_price(self):
        return self.quantity * self.meal.price

