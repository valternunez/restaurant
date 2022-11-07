from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    client_phone = PhoneNumberField(null=False, blank=False, unique=False)
    client_address = models.CharField(max_length=300)
    client_name = models.CharField(max_length=100, blank=False)
    client_order = models.CharField(max_length=300, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Order #" + str(self.id) + " - " + self.client_name
    