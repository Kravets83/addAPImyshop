from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import BaseUser


class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('id', 'user_name', 'email', 'is_superuser',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    user_name = serializers.CharField(
        label="user_name",
        write_only=True
    )
    password = serializers.CharField(
        label="password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        user_name = attrs.get('user_name')
        password = attrs.get('password')

        if user_name and password:
            user = authenticate(request=self.context.get('request'),
                                user_name=user_name, password=password)
            if not user:
                msg = 'Access denied: wrong user_name or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "user_name" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs
