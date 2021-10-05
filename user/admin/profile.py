from django.contrib import admin

from user.models import Profile

BASE = ["title", "created_at", "updated_at", "description", ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
