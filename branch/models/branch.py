from django.db import models

from .common import CommonBaseModel


class Branch(CommonBaseModel):
    branch_manager = models.OneToOneField("user.User", on_delete=models.PROTECT)
