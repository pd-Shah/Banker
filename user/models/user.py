from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models

from ..managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    national_code = models.CharField('National Code', max_length=32, unique=True, )
    profile = models.OneToOneField("Profile", null=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'national_code'

    @property
    def title(self):
        return self.national_code
