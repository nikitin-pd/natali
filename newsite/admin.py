from django.contrib import admin
from .models import Service, Order, OrderStatus


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'cost', 'status')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'service_price', 'service_is_active')


admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderStatus)
