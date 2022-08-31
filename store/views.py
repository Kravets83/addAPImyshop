from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from core.settings import NUM_PAGINATION
from .models import Product, Category
from django.db.models import Q




def categories(request):
    return {'categories': Category.objects.all()}



def products(request):
    return {
        'products': Product.objects.all(),
    }


def product_all(request):
    search_query = request.GET.get("search", "")

    if search_query:
        products = Product.objects.filter(Q(model__icontains=search_query)
                                          | Q(manufacturer__icontains=search_query)
                                          | Q(description__icontains=search_query))
        print(products)
    else:
        products = Product.products.all()
    products_paginator = Paginator(products, NUM_PAGINATION)
    page_num = request.GET.get('page')

    page = products_paginator.get_page(page_num)
    comtext = {
        'count': products_paginator.count,
        'page' : page,
        'products': products

    }


    return render(request, 'store/index.html', comtext)#{'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    products_paginator = Paginator(products, NUM_PAGINATION)
    page_num = request.GET.get('page')

    page_cat = products_paginator.get_page(page_num)
    comtext = {
        'count': products_paginator.count,
        'page': page_cat,
        'products': products,
        'category': category

    }
    return render(request, 'store/products/category.html', comtext)#{'category': category, 'products': products})


#
# def search(request):
#     search_query = request.GET.get("search","")
#     if search_query:
#         products_search = Product.objects.filter(model__icontains=search_query)
#     print(products_search)



