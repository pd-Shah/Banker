from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def normalize_national_code(self, national_code):
        """
        normalize and national_code
        """
        # TODO
        # normalize_national_code
        return national_code

    def create_user(self, national_code, password=None):
        """
        Creates and saves a User with the given national_code, date of
        birth and password.
        """
        if not national_code:
            raise ValueError('Users must have an national_code')

        user = self.model(
            national_code=self.normalize_national_code(national_code),
        )

        user.set_password(password)
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, national_code, password=None):
        """
        Creates and saves a superuser with the given national_code, date of
        birth and password.
        """
        user = self.create_user(
            national_code,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
