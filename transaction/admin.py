from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_filter = ['date', 'type']
    list_display = ['owner', 'type', 'date', 'amount']

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = False
        return super(TransactionAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['owner', 'type', 'date', 'amount']
        return self.readonly_fields


admin.site.register(Transaction, TransactionAdmin)
