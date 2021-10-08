from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from Banker.settings.permissions import ACCOUNT_CAN_DELETE_ALLOWED
from account.models import Account


class CanDelete(BasePermission):

    def has_permission(self, request, view, ):
        group_set = {g.name for g in request.user.groups.all()}
        account_id = request.data.get("account_id", None)
        if account_id is not None:
            if len(group_set.intersection(ACCOUNT_CAN_DELETE_ALLOWED)):
                account = get_object_or_404(Account, pk=account_id)
                if request.user.branch.id == account.branch.id:
                    return True
        return False
