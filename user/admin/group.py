from django.contrib import admin
from django.contrib.auth.models import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
