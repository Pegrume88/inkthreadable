from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.db.models import Q
from django.contrib import messages
from .filters import ProductFilter, SearchFilter



def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    search_filter = SearchFilter(request.GET, queryset=products)
    
    context = {
        'products': products,
        'product_filter': product_filter,
        'search_filter': search_filter,
        
        
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)