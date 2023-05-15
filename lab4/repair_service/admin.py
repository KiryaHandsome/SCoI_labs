from django.contrib import admin
from django import forms

from .models import (
    OrderService,
    ServiceTag,
    Customer,
    Service,
    Order,
)

admin.site.register(Customer)
admin.site.register(ServiceTag)
admin.site.register(Service)


# ability to make orders in admin page
class OrderServiceInlineFormset(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.can_delete = False

    def clean(self):
        super().clean()


class OrderServiceInline(admin.TabularInline):
    model = OrderService
    formset = OrderServiceInlineFormset
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderServiceInline]
