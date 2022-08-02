from django.contrib import admin

from .models import BaseUser

# admin.site.register(BaseUser)

@admin.register(BaseUser)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'user_name', 'is_active', 'is_staff']
    list_editable = ['is_active']
