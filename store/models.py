from django.db import models
from django.urls import reverse


class User(models.Model):
    pass


class Category(models.Model):
    name = models.CharField(max_length=120, db_index=True)
    slug = models.SlugField(max_length=225, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, db_constraint=models.CASCADE, related_name='product_creator',on_delete=models.CASCADE)
    model = models.CharField(max_length=225)
    creator = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=225)
    prise = models.DecimalField(max_digits=7, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'products'
        ordering = ('-created',)

    def __str__(self):
        return self.model
