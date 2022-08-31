from rest_framework import serializers

from .models import Product, Category


class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField('name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'model', 'manufacturer', 'price', 'category')

class ProductDetailSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField('name', read_only=True)
    created_by = serializers.SlugRelatedField('email', read_only=True)

    class Meta:
        model = Product
        fields = ('id','model', 'manufacturer', 'price', 'slug','created_by', 'description', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


