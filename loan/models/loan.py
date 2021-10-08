import json

from django.db import models

from loan.logics import (
    calculate_monthly_refund,
)
from .common import CommonBaseModel

REFUND_TYPES = (
    ('12MONTH', '12MONTH'),
    ('24MONTH', '24MONTH'),
)

STATUS_TYPES = (
    ('Payed', 'Payed'),
    ('In Progress', 'In Progress'),
)


class Loan(CommonBaseModel):
    account = models.ForeignKey("account.Account", on_delete=models.PROTECT, )
    total_months = models.IntegerField()
    value = models.FloatField()
    value_after_profit = models.FloatField()
    type = models.CharField(
        choices=REFUND_TYPES,
        max_length=32,
    )
    status = models.CharField(
        choices=STATUS_TYPES,
        max_length=32,
        default='In Progress'
    )
    loan_detail = models.JSONField(
        null=True,
    )
    monthly_refund_value = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.pk:
            loan_value = self.value
            profit = 10 if self.type == "12MONTH" else 20
            total_months = 12 if self.type == "12MONTH" else 24
            self.monthly_refund_value = calculate_monthly_refund(
                loan_value, profit, total_months
            )

            json_data = []
            for month in range(total_months):
                json_data = json_data.add(
                    {month: {"name": f"{month}' month ", "status": "pending", "pay_date": "0", }}
                )

            self.loan_detail = json.dumps(json_data)

            super().save(*args, **kwargs)
