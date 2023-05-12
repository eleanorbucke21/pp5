from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'
