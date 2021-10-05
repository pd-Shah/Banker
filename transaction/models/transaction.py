from django.db import models

from .common import CommonBaseModel

TRANSACTION_TYPES = (
    ('deposit', 'deposit'),
    ('withdraw', 'withdraw'),
)


class Transaction(CommonBaseModel):
    account = models.ForeignKey("account.Account", on_delete=models.PROTECT, )
    branch = models.ForeignKey("branch.Branch", on_delete=models.PROTECT, )
    init_value = models.FloatField()
    value = models.FloatField()
    type = models.CharField(choices=TRANSACTION_TYPES, max_length=32, )
    final_value = models.FloatField()

    @property
    def title(self, ):
        return str(self.account) + "-->" + str(self.type) + "-->" + str(self.value)
