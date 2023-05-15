from django.db import models

from repair_service.models.service_tag import ServiceTag


class Service(models.Model):
    name = models.CharField(max_length=128,
                            primary_key=True,
                            help_text='Name of service')

    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                help_text='Cost of service')

    about = models.CharField(max_length=256,
                             default='Empty description',
                             help_text='Full description of service')

    service_tags = models.ManyToManyField(ServiceTag)

    def __str__(self):
        return self.name
