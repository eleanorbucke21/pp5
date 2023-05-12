from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'question_categories',
        'message',
    ]


admin.site.register(Contact, ContactAdmin)