from django.db import models
import uuid
from django.utils import timezone


def generate_unique_id():
    return uuid.uuid4()


class Bill(models.Model):
    bill_id = models.UUIDField(primary_key=True, default=generate_unique_id, editable=False)
    bill_user = models.ForeignKey('User', on_delete=models.CASCADE) 
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(null=True, blank=True)

    def set_payment_date(self):
        self.payment_date = timezone.now()
        self.is_paid = True


class Meal(models.Model):
    meal_id = models.UUIDField(primary_key=True, default=generate_unique_id, editable=False)
    name_meal = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name_meal


class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=generate_unique_id, editable=False)
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE)  # ربط بالفئة Bill
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE)  # ربط بالفئة Meal
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} - {self.meal.name_meal}"


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=generate_unique_id, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  
    is_loggedin = models.BooleanField(default=False)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.username
