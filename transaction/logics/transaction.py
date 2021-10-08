from django.db import transaction
from django.shortcuts import get_object_or_404

from account.models import Account
from branch.models import Branch
from ..models import Transaction


def create_transaction(user, destination_id, value, branch_id, ):
    with transaction.atomic():
        source = get_object_or_404(Account, pk=user.account.id)
        destination = get_object_or_404(Account, pk=destination_id)
        branch = get_object_or_404(Branch, pk=branch_id)

        source_final_value, destination_final_value = Transaction.create_transaction(source, destination, branch,
                                                                                     value)

        source.balance = source_final_value
        source.save()

        destination.balance = destination_final_value
        destination.save()
