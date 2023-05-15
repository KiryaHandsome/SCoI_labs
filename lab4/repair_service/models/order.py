from django.db import models

from repair_service.models import Customer, Service


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, through='OrderService')
    created_at = models.DateTimeField(auto_now=True, help_text='Date and time when order was created')

    def __str__(self):
        return f'Order #{self.id}'
