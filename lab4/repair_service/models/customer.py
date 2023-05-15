from django.core.validators import (MinLengthValidator,
                                    MaxLengthValidator,
                                    MinValueValidator)
from django.db import models


class Customer(models.Model):
    full_name = models.CharField(max_length=128,
                                 validators=[MinLengthValidator(1), MaxLengthValidator(128)],
                                 help_text='First and last name of customer')

    address = models.CharField(max_length=256, help_text='Full address of customer')
    passport_id = models.IntegerField(validators=[MinValueValidator(1)],
                                      help_text='Numerical part of id')

    passport_series = models.CharField(max_length=2,
                                       default='KH',
                                       help_text='Literal part of id')

    def __str__(self):
        return f'{self.full_name}'
