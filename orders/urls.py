from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'orders'

urlpatterns = [

    path('add/', views.add, name='add'),


]
