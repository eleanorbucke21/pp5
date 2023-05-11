from django.shortcuts import render
from django.urls import path
from . import views


def view_contact(request):
    """ A view that renders the contact us page"""

    return render(request, 'contact/contact_us.html')