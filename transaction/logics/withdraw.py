from django.db import transaction
from django.shortcuts import get_object_or_404

from account.models import Account
from ..models import Transaction


def create_withdraw(user, value, branch_id):
    with transaction.atomic():
        source = get_object_or_404(Account, pk=user.account.id)
        final_value = Transaction.create_withdraw(source, branch_id, value)
        source.balance = final_value
        source.save()
