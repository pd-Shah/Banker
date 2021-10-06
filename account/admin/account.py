from django.contrib import admin

from ..models import Account

BASE = ['user', 'branch', "description", "created_at", "updated_at", ]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = ["title", "balance"] + BASE
    readonly_fields = ["balance", ]
