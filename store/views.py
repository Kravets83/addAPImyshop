from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category


def categories(request):
    return {'categories': Category.objects.all()}



def products(request):
    return {
        'products': Product.objects.all(),
    }


def product_all(request):
    products = Product.products.all()
    products_paginator = Paginator(products, 2)
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
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
