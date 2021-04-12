from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['phone_number', 'card_number', 'last_name']
    list_display = ['first_name', 'last_name', 'phone_number', 'card_number']
    readonly_fields = ['balance', 'card_number']
    fields = ['first_name', 'last_name', 'phone_number', 'balance', 'card_number']


admin.site.register(Client, ClientAdmin)
