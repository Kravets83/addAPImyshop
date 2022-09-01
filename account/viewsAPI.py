'''API'''
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BaseUser
from .serializer import UsersListSerializer, UserSerializer


class UsersList(APIView):
    """All users list"""

    def get(self, request):
        users = BaseUser.objects.all()
        serializer = UsersListSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    """All about product"""

    def get(self, request, pk):
        user = BaseUser.objects.get(id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    # class AddProduct(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = BaseUser.objects.get(pk=pk)
            user.delete()
            return HttpResponse(status=204)
        except BaseUser.DoesNotExist:
            return HttpResponse(status=404)

    def put(self, request, pk):
        user = BaseUser.objects.get(id=pk)
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
