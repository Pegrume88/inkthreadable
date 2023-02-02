from django.shortcuts import render, get_object_or_404
from .models import Product
from .filters import ProductFilter



def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)

    context = {
        'products': products,
        'product_filter': product_filter,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)