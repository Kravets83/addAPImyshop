from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    preserve_filters = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['model', 'creator', 'slug', 'prise', 'in_stock',
                    'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['prise', 'in_stock']
    preserve_filters = {'slug': ('model',)}
