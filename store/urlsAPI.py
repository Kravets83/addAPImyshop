from django.urls import path

from . import viewsAPI

app_name = 'store'

urlpatterns = [
    # '''API'''
    # '''Product'''
    path('products/', viewsAPI.ProductList.as_view()),
    path('product/<int:pk>', viewsAPI.ProductDetail.as_view()),
    path('product/', viewsAPI.ProductDetail.as_view()),
    # '''Category'''
    path('categorys/', viewsAPI.ListCategory.as_view()),
    path('category/<int:pk>', viewsAPI.CategoryDetail.as_view()),
    path('category/', viewsAPI.CategoryDetail.as_view()),

    path('product_by_category/<int:pk>', viewsAPI.ProductByCategory.as_view()),



]
