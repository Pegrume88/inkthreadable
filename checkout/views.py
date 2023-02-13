from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There are No items in your cart")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MMUpWKYuNOljO3YrQzg7osGRgpW2QX7uaxXj7rbDbdb1VAzctu4wMJMjHNVSQFK5k6238uyuPrZRezumOozf7Sr00hpxTTw1s',
        'client_secret': 'test client secret'
        
    }

    return render(request, template, context)