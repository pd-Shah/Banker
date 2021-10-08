from django.contrib import admin

from ..models import Loan

BASE = ['account', 'value', 'type', 'status', ]


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
