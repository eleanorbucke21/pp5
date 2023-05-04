from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Mrz8TKLJEwf23JVraP5ErxaWdO7nFqrma9jsA07hgT1F4bi8ix2BAIk5mfX2hGC2djWSoMb8LTPpRuJ6oBEZ6ft001TdhQHNb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)