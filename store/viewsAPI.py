'''API'''
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Category
from .serializer import ProductListSerializer, ProductDetailSerializer, ListCategorySerializer


class ProductListView(APIView):
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



class AddProduct(APIView):
    def post(self,request):
        data = JSONParser().parse(request)
        serializer = ProductDetailSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''http://127.0.0.1:8000/api/v1/add_product?"model":"iPhone 12","manufacturer":"apple","price":"900.00",
    "category":"Phone","slug":"iPhone12","created_by":"user@user.com","description":"iPhone 12"'''





class ListCategoryView(APIView):
    """List category"""

    def get(self, request):
        categorys = Category.objects.all()
        serializer = ListCategorySerializer(categorys, many=True)
        return Response(serializer.data)


class ProductByCategoryView(APIView):
    """list products by category"""

    def get(self, request, pk):
        products = Product.objects.filter(category=pk)
        serializer = ProductDetailSerializer(products, many=True)
        return Response(serializer.data)
