from django.db import models

from .common import CommonBaseModel

TRANSACTION_TYPES = (
    ('deposit', 'deposit'),
    ('withdraw', 'withdraw'),
    ('transaction', 'transaction'),
    ('loan', 'loan'),
)


class Transaction(CommonBaseModel):
    source = models.ForeignKey("account.Account", on_delete=models.PROTECT, related_name="source_transaction",
                               null=True, blank=True, )
    destination = models.ForeignKey("account.Account", on_delete=models.PROTECT, related_name="destination_transaction",
                                    null=True, blank=True, )
    branch = models.ForeignKey("branch.Branch", on_delete=models.PROTECT, )
    init_value = models.PositiveIntegerField()
    value = models.PositiveIntegerField()
    type = models.CharField(choices=TRANSACTION_TYPES, max_length=32, )
    final_value = models.PositiveIntegerField()

    @property
    def title(self, ):
        return str(self.source) + " to " + str(self.destination)

    @staticmethod
    def create_deposit(destination, branch_id, value):
        transaction = Transaction.objects.create(
            destination=destination,
            branch_id=branch_id,
            init_value=destination.balance,
            value=value,
            type="deposit",
            final_value=destination.balance + value,
        )
        transaction.save()
        return destination.balance + value

    @staticmethod
    def create_withdraw(source, branch_id, value):
        transaction = Transaction.objects.create(
            source=source,
            branch_id=branch_id,
            init_value=source.balance,
            value=value,
            type="withdraw",
            final_value=source.balance - value,
        )
        transaction.save()
        return source.balance - value

    @staticmethod
    def create_transaction(source, destination, branch, value):
        transaction = Transaction.objects.create(
            destination=destination,
            source=source,
            branch=branch,
            init_value=source.balance,
            value=value,
            type="transaction",
            final_value=source.balance - value,
        )
        transaction.save()
        return source.balance - value, destination.balance + value
