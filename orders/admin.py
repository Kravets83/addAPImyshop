from django.contrib import admin

from .models import Order, OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)

# @admin.register(Order)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ['user', 'created', 'billing_status', 'amount_pay']
#     list_editable = ['billing_status']