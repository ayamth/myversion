from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Orders
from bills.models import Bill

@receiver(post_save, sender=Orders)
def create_bill(sender, instance, created, **kwargs):
    if created and not instance.bill:  # Only create a bill if one doesn’t already exist
        total_amount = instance.get_total_price()
        
        # Create a new Bill for the order
        bill = Bill.objects.create(
            customer=instance.customer,
            total_amount=total_amount,
            payment_status='unpaid'
        )
        
        # Associate the new bill with the order
        instance.bill = bill
        instance.save()

