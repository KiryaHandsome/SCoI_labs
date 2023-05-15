from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    passport_id = models.IntegerField()

    def __str__(self):
        return self.full_name
