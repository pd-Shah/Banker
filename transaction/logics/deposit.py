from django.db import transaction
from django.shortcuts import get_object_or_404

from account.models import Account
from ..models import Transaction


def create_deposit(user, branch_id, value):
    with transaction.atomic():
        destination = get_object_or_404(Account, pk=user.account.id)
        final_value = Transaction.create_deposit(destination, branch_id, value)
        destination.balance = final_value
        destination.save()
