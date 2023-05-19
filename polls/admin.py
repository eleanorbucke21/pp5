from django.contrib import admin
from .models import Poll


class PollsAdmin(admin.ModelAdmin):
    list_display = ['question',]
    actions = ['approve_polls']

    def approve_polls(self, request, queryset):
        queryset.update(approved=True)


admin.site.register(Poll, PollsAdmin)
