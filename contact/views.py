from django.shortcuts import render, redirect, reverse
from django.urls import path
from . import views
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


def contact(request):
    """ Contact Form """
    form = ContactForm
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'question_categories': form.cleaned_data['question_categories'],  # noqa
                    'message': form.cleaned_data['message'],
            }
            contact = form.save()
            messages.success(request, f'Query sent')
            return redirect(reverse('home'))
        else:
            form = ContactForm()

    return render(request, "contact/contact_us.html", {'form': form})
