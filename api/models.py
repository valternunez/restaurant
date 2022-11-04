from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
        client_phone = PhoneNumberField(null=False, blank=False, unique=True)
        client_address = models.CharField(max_length=150)
        client_name = models.CharField(max_length=50)
        client_order = models.CharField(max_length=100)
        
        def __str__(self):
            return "Order #" + str(self.id)