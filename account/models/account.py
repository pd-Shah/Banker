from django.db import models

from .common import CommonBaseModel


class Account(CommonBaseModel):
    user = models.OneToOneField("user.User", on_delete=models.PROTECT, unique=True, )
    branch = models.ForeignKey("branch.Branch", on_delete=models.PROTECT, )
    is_active = models.BooleanField(default=True, )
    balance = models.PositiveIntegerField()

    class Meta:
        unique_together = ('branch', 'user',)

    @property
    def title(self, ):
        return str(self.branch) + "-->" + str(self.user)
