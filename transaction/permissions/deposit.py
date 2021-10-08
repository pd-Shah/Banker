from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from account.models import Account


class CanDeposit(BasePermission):

    def has_permission(self, request, view):
        destination_account_id = request.user.account.id
        if destination_account_id is not None:
            destination_account = get_object_or_404(Account, pk=destination_account_id)
            if destination_account.is_active:
                return True
        return False
