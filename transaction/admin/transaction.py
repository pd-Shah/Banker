from django.contrib import admin

from ..models import Transaction

BASE = ['account', 'branch', 'init_value', 'value', 'type',
        'final_value', "created_at", "updated_at", ]


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = ["title", ] + BASE
