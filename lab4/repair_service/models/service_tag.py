from django.db import models


class ServiceTag(models.Model):
    name = models.CharField(max_length=64,
                            help_text='Tag of service',
                            primary_key=True)

    def __str__(self):
        return self.name
