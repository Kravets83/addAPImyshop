'''API'''
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .serializer import ProductListSerializer, ProductDetailSerializer, CategorySerializer


class ProductList(APIView):
    """All products list"""

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    """All about product"""

    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    # class AddProduct(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProductDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return HttpResponse(status=204)
        except Product.DoesNotExist:
            return HttpResponse(status=404)

    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        data = JSONParser().parse(request)
        serializer = ProductDetailSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class ListCategory(APIView):
    """List category"""

    def get(self, request):
        categorys = Category.objects.all()
        serializer = CategorySerializer(categorys, many=True)
        return Response(serializer.data)


class CategoryDetail(APIView):
    """All about product"""

    def get(self, request, pk):
        product = Category.objects.get(id=pk)
        serializer = CategorySerializer(product)
        return Response(serializer.data)

    # class AddProduct(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return HttpResponse(status=204)
        except Product.DoesNotExist:
            return HttpResponse(status=404)

    def put(self, request, pk):
        category = Category.objects.get(id=pk)
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


class ProductByCategory(APIView):
    """list products by category"""

    def get(self, request, pk):
        products = Product.objects.filter(category=pk)
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)
