from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as gl
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, user_name, password, **fields):
        fields.setdefault('is_staff', True)
        fields.setdefault('is_superuser', True)
        fields.setdefault('is_active', True)

        if fields.get('is_staff') is not True:
            raise ValueError(
                "Superuser is_staff=false")
        if fields.get('is_superuser') is not True:
            raise ValueError(
                "Superuser is_superuser=false")
        if fields.get('is_active') is not True:
            raise ValueError(
                "Superuser is_active=false")

        return self.create_user(self, email, user_name,  password, **fields)

    def create_user(self, email, user_name,  password, **fields):

        if not email:
            raise ValueError(gl('Enter email'))
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name,**fields)

        user.set_password(password)
        user.save()
        return user

class BaseUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(gl('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(gl('about'), max_length=500, blank=True)
    country = CountryField()
    phone_number = PhoneNumberField(blank=True)
    postcode = models.CharField(max_length=150, blank=True)
    address_line1 = models.CharField(max_length=150, blank=True)
    address_line2 = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = 'Accounts'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.user_name













