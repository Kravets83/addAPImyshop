from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    preserve_filters = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['model', 'manufacturer', 'slug', 'price', 'in_stock','is_active',
                    'created', 'updated','get_image']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock', 'is_active']
    preserve_filters = {'slug': ('model',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60">')
        else:
            return "No image"

    get_image.short_description = "IMAGE"
