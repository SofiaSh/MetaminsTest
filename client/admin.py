from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['phone_number', 'card_number', 'last_name']
    list_display = ['first_name', 'last_name', 'phone_number', 'card_number']
    fields = ['first_name', 'last_name', 'phone_number', 'balance', 'card_number', 'password']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['balance', 'card_number']
        return self.readonly_fields

    def get_fieldsets(self, request, obj=None):
        if obj:
            if 'password' in self.fields:
                self.fields.remove('password')
        else:
            if not 'password' in self.fields:
                self.fields.append('password')
        return ((None, {'fields': self.fields}),)


admin.site.register(Client, ClientAdmin)
