from django.urls import path
from . import viewsAPI

app_name = 'account'

urlpatterns = [

    path('users/', viewsAPI.UsersList.as_view()),
    path('user/', viewsAPI.UserDetail.as_view()),
    path('user/<int:pk>', viewsAPI.UserDetail.as_view()),
    path('login/', viewsAPI.LoginView.as_view()),

]
