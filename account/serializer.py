from rest_framework import serializers

from .models import BaseUser


class UsersListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ('id', 'user_name', 'email', 'is_superuser', )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseUser
        fields = '__all__'