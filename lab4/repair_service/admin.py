from django.contrib import admin

from repair_service.models import (
    ServiceTag,
    Service,
)

admin.site.register(ServiceTag)
admin.site.register(Service)
