from django.shortcuts import get_object_or_404

from ..models import Account


def delete_account(pk, ):
    obj = get_object_or_404(Account, pk=pk)
    obj.is_active = False
    obj.save()
