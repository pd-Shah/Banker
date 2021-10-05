from django.contrib import admin

from ..models import Branch

BASE = ["title", "description", "created_at", "updated_at", ]


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
