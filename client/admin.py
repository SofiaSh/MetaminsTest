from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['phone_number', 'card_number', 'last_name']
    list_display = ['phone_number']
    fields = ['first_name', 'last_name', 'phone_number']


admin.site.register(Client, ClientAdmin)
