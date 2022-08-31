from django.urls import path

from . import viewsAPI

app_name = 'store'

urlpatterns = [
    # '''API'''
    path('products/', viewsAPI.ProductListView.as_view()),
    path('product/<int:pk>', viewsAPI.ProductDetail.as_view()),
    path('list_category/', viewsAPI.ListCategoryView.as_view()),
    path('product_by_category/<int:pk>', viewsAPI.ProductByCategoryView.as_view()),
    path('add_product', viewsAPI.AddProduct.as_view()),


]
