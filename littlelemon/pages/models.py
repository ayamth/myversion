from django.db import models

# Create your models here.
import datetime
import uuid

def generate_unique_id():
    return str(uuid.uuid4())
unique_id = generate_unique_id()

class Bill:
    def __init__(self, user_id, total_amount, id = unique_id):
        self.id = id
        self.user_id = user_id
        self.total_amount = total_amount
        self.date = datetime.datetime.now()
        self.is_paid = False
        self.payment_date = None

    

    def set_payment_date(self):
        self.payment_date = datetime.datetime.now()
        self.is_paid = True

class Meal:
    def __init__(self, name, price, id=unique_id):
        self.id = id
        self.name_meal = name
        self.price = price

class Order:
    def __init__(self, bill_id, meal_id, quantity, price, id=unique_id) -> None:
        self.id = id
        self.bill_id = bill_id
        self.meal_id = meal_id
        self.quantity = quantity
        self.price = price

class User:
    def __init__(
        self, first_name, last_name, age, username, password, role, id=unique_id) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.username = username
        self.password = password
        self.is_loggedin = False
        self.role = role

