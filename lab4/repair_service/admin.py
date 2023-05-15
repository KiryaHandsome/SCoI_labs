from django.contrib import admin
from repair_service.models import Customer
from repair_service.models import Service
from repair_service.models import ServiceType

admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(ServiceType)

